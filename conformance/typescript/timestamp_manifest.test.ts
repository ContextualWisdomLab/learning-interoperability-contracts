import assert from "node:assert/strict";
import { readFileSync } from "node:fs";

type TimestampCase = {
  case_name: string;
  timestamp_value: string;
  expected_valid: boolean;
  failure_class: null | "lexical" | "calendar";
};

const caseNames = new Set([
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
]);

function isContractTimestamp(value: string): boolean {
  const match = /^(\d{4})-(\d{2})-(\d{2})[Tt](\d{2}):(\d{2}):(\d{2})(?:\.\d+)?(?:[Zz]|[+-](\d{2}):(\d{2}))$/.exec(value);
  if (!match) return false;

  const [year, month, day, hour, minute, second] = match.slice(1, 7).map(Number);
  const offsetHour = Number(match[7] ?? 0);
  const offsetMinute = Number(match[8] ?? 0);
  const leap = year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0);
  const daysInMonth = [0, 31, leap ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

  return (
    year > 0 &&
    month >= 1 &&
    month <= 12 &&
    day >= 1 &&
    day <= daysInMonth[month] &&
    hour <= 23 &&
    minute <= 59 &&
    second <= 59 &&
    offsetHour <= 23 &&
    offsetMinute <= 59
  );
}

function validateTimestampManifest(manifest: string) {
  const document = JSON.parse(manifest) as {
    fixture_contract?: unknown;
    timestamp_cases?: unknown;
  };
  assert.equal(document.fixture_contract, "learning_event_timestamp_v1");
  assert.ok(Array.isArray(document.timestamp_cases));

  const cases = document.timestamp_cases as TimestampCase[];
  assert.deepEqual(new Set(cases.map(({ case_name }) => case_name)), caseNames);
  for (const timestampCase of cases) {
    assert.deepEqual(Object.keys(timestampCase).sort(), [
      "case_name",
      "expected_valid",
      "failure_class",
      "timestamp_value",
    ]);
    assert.equal(
      isContractTimestamp(timestampCase.timestamp_value),
      timestampCase.expected_valid,
      timestampCase.case_name,
    );
  }

  const validCount = cases.filter(({ expected_valid }) => expected_valid).length;
  return {
    caseCount: cases.length,
    validCount,
    invalidCount: cases.length - validCount,
  };
}

const manifest = readFileSync("fixtures/v1/timestamp_format_cases.json", "utf8");

assert.deepEqual(validateTimestampManifest(manifest), {
  caseCount: 16,
  validCount: 5,
  invalidCount: 11,
});

assert.throws(() =>
  validateTimestampManifest(manifest.replace('"expected_valid": false', '"expected_valid": true')),
);
