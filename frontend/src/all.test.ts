import { expect, test } from "vitest";
import { formatDatetime } from "./lib/utils";

test("formatDateTime", () => {
  let dateTime = "2025-12-01T12:30:00";
  expect(formatDatetime(dateTime)).toEqual("01/12/25 12:30");
});
