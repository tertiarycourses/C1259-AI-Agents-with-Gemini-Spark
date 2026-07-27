# Lab 8 — Design Schedules and Conditional Triggers

**Topic 03:** Building Reusable Skills and Schedules  |  **Day 2**  |  **Approx. 40 min**  |  **Course:** AI Agents with Gemini Spark (C1259)

> **Connected project:** this lab adds one more automation to the **Brightwave AI operations assistant** you began in Lab 1. If you fell behind, use the supplied Brightwave sample data to rejoin at this lab.

## Goal

Schedule a skill to run automatically on a cadence and add a trigger that runs only when a condition is met.

## What you'll build

A scheduled daily inbox digest and one conditional trigger, both tested.

**Tools and techniques:** Schedules, cadence, conditional triggers, event conditions, approvals on automation

## Prerequisites

- Lab 5 (inbox summary) and Lab 7 (a saved skill) complete.
- A key sender's email address to use for the conditional trigger (or the Brightwave sample).

## Steps

### Step 1

Take your inbox-summary instruction from Lab 5 and set it to run on a schedule.

Instruction to give the agent (paste into Gemini Spark):

```text
Every weekday at 8:00am, summarise my unread emails as Urgent / Needs a reply / FYI and put the digest in a Doc named 'Daily Digest'.
```

### Step 2

Choose the cadence and time deliberately — early enough to be useful, not so early the inbox is empty.

### Step 3

Decide the approval posture for scheduled runs: reading and drafting can run unattended; sending or sharing should still need approval. Set it.

### Step 4

Test the schedule without waiting a day: use the 'run now' option to fire it once and confirm the digest Doc is created.

### Step 5

Now build a conditional trigger. Choose a condition that matters and a safe action (draft, don't send).

Instruction to give the agent (paste into Gemini Spark):

```text
When a new email arrives from <KEY CLIENT EMAIL>, draft a holding reply saying we'll respond within one business day. Save as draft; do not send.
```

### Step 6

Test the trigger safely: send yourself a test email that meets the condition (or use the sample), and confirm the draft is created.

### Step 7

Check the activity log to see the scheduled run and the triggered run recorded as separate entries.

### Step 8

Set a stop rule: note how you would pause or delete a schedule or trigger if it ever misbehaves.

## Test it

Your inbox digest runs on its schedule (verified with 'run now') and your conditional trigger creates a draft only when the condition is met — both visible as entries in the activity log.

## Troubleshooting

- **You don't want to wait a day to test the schedule.** Use 'run now' to fire the scheduled skill once and confirm it produces the digest, then leave the schedule to run on its cadence.
- **The trigger fired for the wrong emails.** Tighten the condition, e.g. exact sender address, and re-test with one matching and one non-matching email.
- **A scheduled run tried to send something.** Set scheduled runs to draft-only; require approval for send/share even on automation. Verify in the activity log.

## Challenge

Add a second schedule — an end-of-day 'what's still unanswered' digest — and make sure the two don't overlap confusingly.

## Reflection

LO5 — Which of your automations is safe to run fully unattended, and which must always pause for approval?

## Deliverable

Save your output — it becomes part of your **AI operations assistant**, the connected toolkit you consolidate, monitor and plan to scale in Lab 12.

---

*AI Agents with Gemini Spark (C1259) · C1259 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
