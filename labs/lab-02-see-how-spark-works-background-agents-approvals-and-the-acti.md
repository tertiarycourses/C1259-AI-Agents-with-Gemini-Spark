# Lab 2 — See How Spark Works — Background Agents, Approvals and the Activity Log

**Topic 01:** Getting Started with AI Agents and Gemini Spark  |  **Day 1**  |  **Approx. 45 min**  |  **Course:** AI Agents with Gemini Spark (C1259)

> **Connected project:** this lab adds one more automation to the **Brightwave AI operations assistant** you began in Lab 1. If you fell behind, use the supplied Brightwave sample data to rejoin at this lab.

## Goal

Run a background task, use the approval gate, and inspect and undo actions from the activity log.

## What you'll build

A drafted (not sent) email held at the approval gate, plus a reviewed activity-log entry you can undo.

**Tools and techniques:** Background agents, approval gate, activity log, undo, Gmail draft

## Prerequisites

- Lab 1 complete: Spark connected, approvals ON.
- At least one email in your inbox to reply to (or use the Brightwave sample).

## Steps

### Step 1

Give the agent a task that prepares a change but must stop for approval: draft (do not send) a short reply to your most recent email.

Instruction to give the agent (paste into Gemini Spark):

```text
Draft a brief, friendly reply to my most recent email. Save it as a draft. Do not send it.
```

### Step 2

While it works, start a second, unrelated read task so you can see a background agent working alongside you.

Instruction to give the agent (paste into Gemini Spark):

```text
Separately, summarise the subjects of my last 5 emails in one line each.
```

### Step 3

Return to the reply task and find the approval gate: the agent has prepared a draft and is waiting for your decision. Read the draft.

### Step 4

Do NOT approve sending. Choose the option that keeps it as a draft only, then open Gmail and confirm the draft exists and was not sent.

### Step 5

Open the activity log (the agent's history of actions). Find the entry for the draft you just created.

### Step 6

Open that log entry and read exactly what the agent did, which app it touched, and when. This is your audit trail.

### Step 7

Practise undo: use the log to undo or discard the draft. Confirm in Gmail that the draft is gone.

### Step 8

Write one sentence in your own notes: what will you always check in the activity log before you approve an action?

## Test it

You created a reply as a draft only (never sent), located and read its entry in the activity log, and successfully undid it — confirming the draft no longer exists in Gmail.

## Troubleshooting

- **The agent sent the email instead of drafting it.** Your instruction must say 'Save as a draft. Do not send.' Re-run with that limit, and check the activity log to confirm nothing was sent.
- **You can't find the activity log.** It is the agent's history/activity area. If unsure, ask the agent: 'Show me what you just did.' Then locate the same action in the log UI.
- **Undo isn't available for an action.** Not every action is auto-reversible. For a draft, delete it in Gmail. This is exactly why the approval gate matters before an action is taken.

## Challenge

Start three read-only tasks at once and watch them run as background agents. Note which finishes first and whether order matters.

## Reflection

LO4 — What will you always check in the activity log before you approve an action that sends or shares something?

## Deliverable

Save your output — it becomes part of your **AI operations assistant**, the connected toolkit you consolidate, monitor and plan to scale in Lab 12.

---

*AI Agents with Gemini Spark (C1259) · C1259 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
