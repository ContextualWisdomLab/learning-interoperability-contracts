use std::collections::HashSet;

const MANIFEST: &str = include_str!("../../fixtures/v1/timestamp_format_cases.json");

const CASE_NAMES: [&str; 16] = [
    "valid_utc_uppercase",
    "valid_utc_lowercase",
    "valid_leap_day_maximum_offset",
    "valid_negative_half_hour_offset",
    "valid_fractional_seconds",
    "invalid_date_only",
    "invalid_non_date",
    "invalid_missing_offset",
    "invalid_non_leap_day",
    "invalid_month",
    "invalid_month_day",
    "invalid_hour_24",
    "invalid_minute_60",
    "invalid_leap_second",
    "invalid_offset_hour_24",
    "invalid_offset_minute_60",
];

fn json_string<'a>(line: &'a str, key: &str) -> Option<&'a str> {
    let prefix = format!("\"{key}\": \"");
    let value = line.trim().strip_prefix(&prefix)?;
    let value = value.strip_suffix(',').unwrap_or(value).strip_suffix('"')?;
    (!value.contains(['"', '\\'])).then_some(value)
}

fn parse_digits(value: &[u8]) -> Option<u32> {
    value.iter().try_fold(0_u32, |number, digit| {
        digit
            .is_ascii_digit()
            .then(|| number * 10 + u32::from(digit - b'0'))
    })
}

fn is_leap_year(year: u32) -> bool {
    year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)
}

fn is_contract_timestamp(value: &str) -> bool {
    let bytes = value.as_bytes();
    if bytes.len() < 20
        || bytes.get(4) != Some(&b'-')
        || bytes.get(7) != Some(&b'-')
        || !matches!(bytes.get(10), Some(b'T' | b't'))
        || bytes.get(13) != Some(&b':')
        || bytes.get(16) != Some(&b':')
    {
        return false;
    }

    let Some(year) = parse_digits(&bytes[0..4]) else {
        return false;
    };
    let Some(month) = parse_digits(&bytes[5..7]) else {
        return false;
    };
    let Some(day) = parse_digits(&bytes[8..10]) else {
        return false;
    };
    let Some(hour) = parse_digits(&bytes[11..13]) else {
        return false;
    };
    let Some(minute) = parse_digits(&bytes[14..16]) else {
        return false;
    };
    let Some(second) = parse_digits(&bytes[17..19]) else {
        return false;
    };

    let days_in_month = match month {
        1 | 3 | 5 | 7 | 8 | 10 | 12 => 31,
        4 | 6 | 9 | 11 => 30,
        2 if is_leap_year(year) => 29,
        2 => 28,
        _ => return false,
    };
    if year == 0 || day == 0 || day > days_in_month || hour > 23 || minute > 59 || second > 59 {
        return false;
    }

    let mut offset = 19;
    if bytes.get(offset) == Some(&b'.') {
        offset += 1;
        let fraction_start = offset;
        while bytes.get(offset).is_some_and(u8::is_ascii_digit) {
            offset += 1;
        }
        if offset == fraction_start {
            return false;
        }
    }

    match bytes.get(offset) {
        Some(b'Z' | b'z') => offset + 1 == bytes.len(),
        Some(b'+' | b'-') if offset + 6 == bytes.len() && bytes[offset + 3] == b':' => {
            matches!(parse_digits(&bytes[offset + 1..offset + 3]), Some(0..=23))
                && matches!(parse_digits(&bytes[offset + 4..offset + 6]), Some(0..=59))
        }
        _ => false,
    }
}

fn validate_timestamp_manifest(manifest: &str) -> (usize, usize, usize) {
    assert_eq!(
        manifest
            .lines()
            .filter(|line| line.trim() == "\"fixture_contract\": \"learning_event_timestamp_v1\",")
            .count(),
        1,
        "fixture contract identity must occur exactly once"
    );

    let mut names = HashSet::new();
    let mut current_name = None;
    let mut current_timestamp = None;
    let mut current_expected = None;
    let mut case_count = 0;
    let mut valid_count = 0;

    for line in manifest.lines() {
        if let Some(value) = json_string(line, "case_name") {
            assert!(
                current_name.replace(value).is_none(),
                "duplicate case_name field"
            );
        } else if let Some(value) = json_string(line, "timestamp_value") {
            assert!(
                current_timestamp.replace(value).is_none(),
                "duplicate timestamp_value field"
            );
        } else if line.trim().starts_with("\"expected_valid\": ") {
            let value = line
                .trim()
                .strip_prefix("\"expected_valid\": ")
                .and_then(|value| value.strip_suffix(','));
            current_expected = match value {
                Some("true") => Some(true),
                Some("false") => Some(false),
                _ => panic!("expected_valid must be boolean"),
            };
        } else if line.trim().starts_with("\"failure_class\": ") {
            let name = current_name
                .take()
                .expect("case_name must precede failure_class");
            let timestamp = current_timestamp
                .take()
                .expect("timestamp_value must precede failure_class");
            let expected = current_expected
                .take()
                .expect("expected_valid must precede failure_class");
            assert!(names.insert(name), "case names must be unique");
            assert_eq!(
                is_contract_timestamp(timestamp),
                expected,
                "timestamp result differs for {name}"
            );
            case_count += 1;
            valid_count += usize::from(expected);
        }
    }

    assert_eq!(names, CASE_NAMES.into_iter().collect());
    (case_count, valid_count, case_count - valid_count)
}

#[test]
fn unchanged_manifest_matches_timestamp_contract() {
    assert_eq!(validate_timestamp_manifest(MANIFEST), (16, 5, 11));
}

#[test]
fn consumer_detects_inverted_expectation() {
    let mutated = MANIFEST.replacen("\"expected_valid\": false", "\"expected_valid\": true", 1);
    assert!(std::panic::catch_unwind(|| validate_timestamp_manifest(&mutated)).is_err());
}
