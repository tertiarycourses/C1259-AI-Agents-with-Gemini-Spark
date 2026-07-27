# Lab 9 — Chain Multi-Step Workflows and Personalise Your Agent

**Topic 03:** Building Reusable Skills and Schedules  |  **Day 2**  |  **Approx. 35 min**  |  **Course:** AI Agents with Gemini Spark (C1259)

> **Connected project:** this lab adds one more automation to the **Brightwave AI operations assistant** you began in Lab 1. If you fell behind, use the supplied Brightwave sample data to rejoin at this lab.

## Goal

Connect skills so one feeds the next into a single workflow, and personalise the agent so output needs less editing.

## What you'll build

A two-or-three-step chained workflow and a saved personalisation profile for your agent.

**Tools and techniques:** Chaining, multi-step workflows, passing outputs as inputs, personalisation, preferences, style profile

## Prerequisites

- Lab 7 (a skill) and Lab 8 (schedules/triggers) complete.
- Two or three skills or instructions that could feed each other.

## Steps

### Step 1

Sketch a short chain on paper first: step 1 produces something step 2 uses. Keep it to two or three steps.

Instruction to give the agent (paste into Gemini Spark):

```text
CHAIN: 1) summarise this week's client emails -> 2) draft a weekly update from that summary -> 3) create a Doc for review.
```

### Step 2

Build step 1 as an instruction (or reuse a skill) that produces a clear, structured output for the next step to consume.

### Step 3

Build step 2 so it explicitly takes step 1's output as its input, rather than starting from scratch.

### Step 4

Add step 3 to place the final result where you want it (a Doc in your Brightwave folder), as a draft for review.

### Step 5

Run the whole chain once and review each hand-off: did step 2 actually use step 1's output? Refine the weak link.

### Step 6

Now personalise the agent. Save a profile of recurring context so you stop repeating yourself.

Instruction to give the agent (paste into Gemini Spark):

```text
Remember: I'm the ops coordinator at Brightwave Studio. Our clients are SMEs. Default tone: warm and brief. Working hours 9-6, Mon-Fri.
```

### Step 7

Re-run one earlier task and confirm the personalisation improved it — less context to type, output closer to your style.

### Step 8

Save the chained workflow so you can run the whole thing next week with one instruction.

## Test it

Running your chained workflow once produces the final Doc with each step visibly using the previous step's output, and your saved personalisation profile measurably reduces how much you have to edit or re-explain.

## Troubleshooting

- **Step 2 ignored step 1's output.** Make the hand-off explicit: 'using the summary from the previous step, draft...'. Name the artifact the next step should read.
- **The chain broke halfway.** Run each step alone first, confirm its output, then reconnect. Check the activity log to see where it stopped.
- **Personalisation didn't change anything.** Save the profile explicitly and re-run a task that depends on that context; confirm you had to type less to get the same result.

## Challenge

Extend the chain to a fourth step that files the final Doc to a specific Drive folder and notifies you — as a draft notification.

## Reflection

LO6 — Which manual sequence of steps in your week would benefit most from being chained into one run?

## Deliverable

Save your output — it becomes part of your **AI operations assistant**, the connected toolkit you consolidate, monitor and plan to scale in Lab 12.

---

*AI Agents with Gemini Spark (C1259) · C1259 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
