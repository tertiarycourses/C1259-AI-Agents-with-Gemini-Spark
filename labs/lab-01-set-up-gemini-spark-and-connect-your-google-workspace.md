# Lab 1 — Set Up Gemini Spark and Connect Your Google Workspace

**Topic 01:** Getting Started with AI Agents and Gemini Spark  |  **Day 1**  |  **Approx. 35 min**  |  **Course:** AI Agents with Gemini Spark (C1259)

## Scenario

Brightwave Studio is a six-person creative agency. You are the operations coordinator: you triage a busy shared inbox, prepare meetings, chase leads, log expenses and pull together weekly reports. There is more routine admin than one person can keep up with. Across this course you build an AI operations assistant in Gemini Spark that takes the routine work off your plate — always under your review. Use this scenario only if you cannot use a real process from your own workplace; your own Workspace is always preferred.

## Goal

Access Gemini Spark, connect it to Gmail, Calendar and Drive, and run a first supervised task.

## What you'll build

A working Gemini Spark connected to Gmail, Calendar and Drive, plus one completed, reviewed first task.

**Tools and techniques:** Gemini Spark, Google account, Gmail, Calendar, Drive, approvals

## Prerequisites

- A Google account with Workspace access (Gmail, Calendar, Drive).
- Gemini Spark enabled on your account — the trainer confirms this at the start of Day 1.
- Chrome or Edge, signed in to the correct Google account.

## Steps

### Step 1

Open gemini.google.com in Chrome or Edge and sign in with the Google account you will use for the course.

### Step 2

Find Gemini Spark (the agent/automation area). If you cannot see it, tell the trainer — access is confirmed at the start of Day 1.

### Step 3

Open the connections/permissions panel and confirm Spark can access Gmail, Calendar and Drive. Grant access to those three only, for now.

### Step 4

Read the approval setting: confirm Spark will ask before it sends email, shares files or edits anything. Leave approvals ON.

### Step 5

Run a first, safe task: ask the agent to list your three next calendar events. This only reads data, so it is a gentle first run.

Instruction to give the agent (paste into Gemini Spark):

```text
List my next 3 calendar events with date, time and title. Do not change anything.
```

### Step 6

Watch how the agent works: it states a plan, carries it out, and shows you the result. Read the result before doing anything else.

### Step 7

Ask one follow-up so you see the agent hold context: have it note which of those events has no agenda yet.

Instruction to give the agent (paste into Gemini Spark):

```text
Of those 3 events, tell me which have no agenda in the description.
```

### Step 8

Confirm nothing was changed in your calendar — this was a read-only task. You have now seen the full loop safely.

## Test it

Gemini Spark is connected to Gmail, Calendar and Drive, approvals are ON, and the agent has returned a correct list of your next three events without changing anything.

## Troubleshooting

- **You can't see Gemini Spark on your account.** Tell the trainer — access is provisioned per account. While you wait, follow the demo and pair with a neighbour who has access.
- **Spark says it can't access Gmail/Calendar/Drive.** Re-open the connections panel and grant access to those three apps. Make sure you granted access for the same Google account you are signed in to.
- **The agent changed something you didn't expect.** This lab is read-only, so it shouldn't. If it did, open the activity log and undo it, then check that approvals are still ON.

## Challenge

Ask the agent to also tell you which of your next five events are external (have guests outside your organisation) — still read-only.

## Reflection

LO1 — In your own words, what is the difference between Gemini answering a question and Gemini acting as an agent on your Workspace?

## Deliverable

Save your output — it becomes part of your **AI operations assistant**, the connected toolkit you consolidate, monitor and plan to scale in Lab 12.

---

*AI Agents with Gemini Spark (C1259) · C1259 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
