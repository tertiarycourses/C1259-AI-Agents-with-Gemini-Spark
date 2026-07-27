# AI Agents with Gemini Spark (C1259) — Learner Guide

**Course Code:** C1259  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v1.0 · 27 July 2026**

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Before You Start — Preparation](#before-you-start--preparation)
- [Topic 01 — Getting Started with AI Agents and Gemini Spark  (25%)](#topic-01--getting-started-with-ai-agents-and-gemini-spark--25)
  - [Lab 1 — Set Up Gemini Spark and Connect Your Google Workspace](#lab-1--set-up-gemini-spark-and-connect-your-google-workspace)
  - [Lab 2 — See How Spark Works — Background Agents, Approvals and the Activity Log](#lab-2--see-how-spark-works--background-agents-approvals-and-the-activity-log)
  - [Lab 3 — Instruct Your Agent — Effective Prompting and a Reusable Instruction Template](#lab-3--instruct-your-agent--effective-prompting-and-a-reusable-instruction-template)
- [Topic 02 — Automating Work with Gemini Spark Tasks  (30%)](#topic-02--automating-work-with-gemini-spark-tasks--30)
  - [Lab 4 — Create One-Off Tasks for Research and Organisation](#lab-4--create-one-off-tasks-for-research-and-organisation)
  - [Lab 5 — Automate Email — Inbox Summaries and Reply Drafting](#lab-5--automate-email--inbox-summaries-and-reply-drafting)
  - [Lab 6 — Work with Docs, Sheets and Slides — Generate, Review and Refine](#lab-6--work-with-docs-sheets-and-slides--generate-review-and-refine)
- [Topic 03 — Building Reusable Skills and Schedules  (25%)](#topic-03--building-reusable-skills-and-schedules--25)
  - [Lab 7 — Create a Custom Reusable Skill — the Ghostwriter](#lab-7--create-a-custom-reusable-skill--the-ghostwriter)
  - [Lab 8 — Design Schedules and Conditional Triggers](#lab-8--design-schedules-and-conditional-triggers)
  - [Lab 9 — Chain Multi-Step Workflows and Personalise Your Agent](#lab-9--chain-multi-step-workflows-and-personalise-your-agent)
- [Topic 04 — Advanced Agentic Workflows and Real-World Automation  (20%)](#topic-04--advanced-agentic-workflows-and-real-world-automation--20)
  - [Lab 10 — Automate Lead Management, Expenses and Planning](#lab-10--automate-lead-management-expenses-and-planning)
  - [Lab 11 — Coordinate Multi-App Workflows and Set Safe-Automation Guardrails](#lab-11--coordinate-multi-app-workflows-and-set-safe-automation-guardrails)
  - [Lab 12 — Monitor, Improve and Scale Your AI Agents](#lab-12--monitor-improve-and-scale-your-ai-agents)
- [Wrap-Up](#wrap-up)
- [Next Steps](#next-steps)
- [Glossary](#glossary)


## Introduction

This Learner Guide accompanies the AI Agents with Gemini Spark (C1259) course, conducted by Tertiary Infotech Academy Pte Ltd. It carries the full detail of all 12 hands-on labs, in the order you will run them, together with the concepts each lab depends on.

The labs build a single, connected 'AI operations assistant' for a small studio called Brightwave. You start it in Lab 1 and add one automation to it in every lab. Wherever you can, use your own Google Workspace so you leave the course with agents that already work for you; a supplied Brightwave sample scenario is provided for anyone who prefers not to use their own data.


## Course Learning Outcomes

- LO1: Explain what autonomous AI agents are and how Gemini Spark's background agents, approvals and controls work.
- LO2: Connect Gemini Spark to Google Workspace and write clear, effective instructions that an agent can act on.
- LO3: Create one-off agent tasks to research, organise, summarise email and draft content across Docs, Sheets and Slides.
- LO4: Review, approve and refine agent actions so automated work stays accurate and under your control.
- LO5: Build custom reusable skills and design schedules and conditional triggers that run automatically.
- LO6: Chain multi-step workflows across several Workspace apps and personalise your agent's behaviour and style.
- LO7: Automate real-world workflows — lead management, expenses and planning — with sound permission and privacy guardrails.
- LO8: Monitor, improve and scale your AI agents responsibly.


## Before You Start — Preparation

**What you need**

- A laptop (Windows or Mac) with a current Chrome or Edge browser.
- A Google account with Google Workspace access to Gmail, Calendar, Drive, Docs, Sheets and Slides.
- Gemini Spark available and enabled on your Google account (the trainer will confirm access at the start of Day 1).
- Optional: a few of your own real (non-confidential) emails, files or notes to automate — or use the supplied Brightwave sample data.

**Verify your setup**

Before Lab 1, confirm you can sign in to Google, open Gemini, and see your Gmail, Calendar and Drive. If Spark is not yet visible on your account, tell the trainer.

```bash
Open gemini.google.com  ·  sign in  ·  confirm Gmail, Calendar and Drive are accessible
```

**Conventions used in every lab**

- Placeholders such as <YOUR NAME> or <SENDER EMAIL> are replaced with your own values.
- Chat/instruction text you give the agent is shown in a shaded box — type or paste it into Spark.
- Every lab ends with a 'Test it' step — an explicit check that the agent did the right thing before you move on.
- Approve nothing you have not read. If a result is wrong, refine the instruction and run it again.


## Topic 01 — Getting Started with AI Agents and Gemini Spark  (25%)

What autonomous agents are · How Spark works · Connecting Workspace · Instructing your agent

**Key concepts**

- Autonomous AI agents — an agent doesn't just answer; it plans and carries out multi-step tasks toward a goal you set.
- Gemini Spark — Google's agentic layer that works across your Workspace apps to get real tasks done for you.
- Background agents — Spark can work through a task on your behalf while you get on with something else.
- Approvals and control — Spark pauses for your approval before it sends, shares or changes anything that matters.
- Connecting Workspace — Spark acts through Gmail, Calendar and Drive using your existing Google account permissions.
- The activity log — every action an agent takes is recorded so you can see, trust and undo what it did.
- Effective instructing — a good instruction states the goal, the inputs, the output and the limits in plain language.
- Prompt vs instruction — a chat prompt asks for text; an agent instruction asks for an outcome you can check.


### Lab 1 — Set Up Gemini Spark and Connect Your Google Workspace

Learning outcome: Access Gemini Spark, connect it to Gmail, Calendar and Drive, and run a first supervised task..

Goal: This lab gets your agent working. You confirm Spark is available on your account, connect it to the Workspace apps it will act through, and run one small, fully supervised task so you can see the instruct-run-review-approve loop end to end before you rely on it. BUILDING BLOCK — the automation you build in this lab is added to your AI operations assistant, the connected toolkit you assemble across all 12 labs.

**What you'll build**

A working Gemini Spark connected to Gmail, Calendar and Drive, plus one completed, reviewed first task.   (Tools: Gemini Spark, Google account, Gmail, Calendar, Drive, approvals.)

**Step-by-step**

1. Open gemini.google.com in Chrome or Edge and sign in with the Google account you will use for the course.
2. Find Gemini Spark (the agent/automation area). If you cannot see it, tell the trainer — access is confirmed at the start of Day 1.
3. Open the connections/permissions panel and confirm Spark can access Gmail, Calendar and Drive. Grant access to those three only, for now.
4. Read the approval setting: confirm Spark will ask before it sends email, shares files or edits anything. Leave approvals ON.
5. Run a first, safe task: ask the agent to list your three next calendar events. This only reads data, so it is a gentle first run.

   ```bash
   List my next 3 calendar events with date, time and title. Do not change anything.
   ```

6. Watch how the agent works: it states a plan, carries it out, and shows you the result. Read the result before doing anything else.
7. Ask one follow-up so you see the agent hold context: have it note which of those events has no agenda yet.

   ```bash
   Of those 3 events, tell me which have no agenda in the description.
   ```

8. Confirm nothing was changed in your calendar — this was a read-only task. You have now seen the full loop safely.

**Test it**

Gemini Spark is connected to Gmail, Calendar and Drive, approvals are ON, and the agent has returned a correct list of your next three events without changing anything.

> **Note:** Full commands and screenshots are in labs/lab-01-*.md. Use only accounts and data you are authorised to use. Never paste real passwords, API keys or confidential personal data into an agent instruction; use the supplied sample data if in doubt.

---


### Lab 2 — See How Spark Works — Background Agents, Approvals and the Activity Log

Learning outcome: Run a background task, use the approval gate, and inspect and undo actions from the activity log..

Goal: Now you learn to trust the agent by watching it closely. You give Spark a task that PROPOSES a change, stop at the approval gate, then approve it — and find the whole thing again in the activity log, where you can review and undo. This is the control model the rest of the course depends on. BUILDING BLOCK — the automation you build in this lab is added to your AI operations assistant, the connected toolkit you assemble across all 12 labs.

**What you'll build**

A drafted (not sent) email held at the approval gate, plus a reviewed activity-log entry you can undo.   (Tools: Background agents, approval gate, activity log, undo, Gmail draft.)

**Step-by-step**

1. Give the agent a task that prepares a change but must stop for approval: draft (do not send) a short reply to your most recent email.

   ```bash
   Draft a brief, friendly reply to my most recent email. Save it as a draft. Do not send it.
   ```

2. While it works, start a second, unrelated read task so you can see a background agent working alongside you.

   ```bash
   Separately, summarise the subjects of my last 5 emails in one line each.
   ```

3. Return to the reply task and find the approval gate: the agent has prepared a draft and is waiting for your decision. Read the draft.
4. Do NOT approve sending. Choose the option that keeps it as a draft only, then open Gmail and confirm the draft exists and was not sent.
5. Open the activity log (the agent's history of actions). Find the entry for the draft you just created.
6. Open that log entry and read exactly what the agent did, which app it touched, and when. This is your audit trail.
7. Practise undo: use the log to undo or discard the draft. Confirm in Gmail that the draft is gone.
8. Write one sentence in your own notes: what will you always check in the activity log before you approve an action?

**Test it**

You created a reply as a draft only (never sent), located and read its entry in the activity log, and successfully undid it — confirming the draft no longer exists in Gmail.

> **Note:** Full commands and screenshots are in labs/lab-02-*.md. Use only accounts and data you are authorised to use. Never paste real passwords, API keys or confidential personal data into an agent instruction; use the supplied sample data if in doubt.

---


### Lab 3 — Instruct Your Agent — Effective Prompting and a Reusable Instruction Template

Learning outcome: Write clear agent instructions and capture a reusable instruction template that gets good results first time..

Goal: An agent is only as good as its instruction. You compare a vague instruction with a specific one, see the difference in the result, then distil what worked into a reusable template — Goal, Inputs, Output, Limits — that you will use for every task from here on. BUILDING BLOCK — the automation you build in this lab is added to your AI operations assistant, the connected toolkit you assemble across all 12 labs.

**What you'll build**

A four-part instruction template and one strong, tested instruction saved for reuse.   (Tools: Instruction design, goal/inputs/output/limits, prompt comparison, refinement.)

**Step-by-step**

1. Run a deliberately vague instruction and note how generic or off-target the result is.

   ```bash
   Sort out my inbox.
   ```

2. Now run a specific instruction for the same intent and compare the result — it should be sharper and more useful.

   ```bash
   Group my unread emails from the last 2 days into: needs a reply, for information, and can archive. List subjects under each.
   ```

3. Write down the four parts that made the second instruction work: the Goal, the Inputs it uses, the Output you want, and the Limits.
4. Capture your reusable template in your notes so every future task follows it.

   ```bash
   GOAL: <what outcome> | INPUTS: <which emails/files/dates> | OUTPUT: <format & where> | LIMITS: <what NOT to do, e.g. do not send>
   ```

5. Add limits that keep you safe by default: never send, share or delete without approval; ignore anything marked confidential.
6. Rewrite one everyday task of your own using the template — for example a weekly status summary — and run it.
7. Refine once: change one part of the instruction (Output or Limits) and re-run to see how the result changes. Keep the better version.
8. Save your best instruction where you can find it again — you will turn it into a reusable skill in Topic 3.

**Test it**

You can show two results for the same intent (vague vs specific), a written four-part instruction template, and one refined instruction that produced the output you specified in the format you asked for.

> **Note:** Full commands and screenshots are in labs/lab-03-*.md. Use only accounts and data you are authorised to use. Never paste real passwords, API keys or confidential personal data into an agent instruction; use the supplied sample data if in doubt.

---


## Topic 02 — Automating Work with Gemini Spark Tasks  (30%)

One-off tasks · Email summaries and drafting · Docs, Sheets and Slides · Reviewing and refining

**Key concepts**

- One-off tasks — a single instruction Spark runs once, ideal for research, clean-up and organising work.
- Research tasks — ask the agent to gather, compare and summarise information into a structured result you can reuse.
- Inbox summaries — Spark reads a busy inbox and hands you a short, prioritised digest of what needs attention.
- Email drafting — the agent drafts replies in your voice and leaves them for you to review before anything is sent.
- Working with Docs — generate outlines, first drafts and formatted documents straight into Google Docs.
- Working with Sheets — turn messy inputs into a clean, structured spreadsheet the agent fills for you.
- Working with Slides — draft a presentation deck from a brief or a document, ready for you to polish.
- Reviewing and refining — you inspect each result, approve the good, and refine the instruction until it is right.


### Lab 4 — Create One-Off Tasks for Research and Organisation

Learning outcome: Use one-off agent tasks to research a topic and to organise emails and Drive files..

Goal: One-off tasks are the workhorse of Spark: a single instruction the agent runs once. You run a research task that returns a structured, reusable result, then an organisation task that tidies your inbox and Drive — reviewing both before you accept them. BUILDING BLOCK — the automation you build in this lab is added to your AI operations assistant, the connected toolkit you assemble across all 12 labs.

**What you'll build**

A structured research brief in a Doc, plus a tidied inbox and a proposed Drive folder structure.   (Tools: One-off tasks, research, summarisation, Gmail labels, Drive organisation, Docs.)

**Step-by-step**

1. Run a research task with a clear output format. Ask for a short, structured brief you can reuse, not a wall of text.

   ```bash
   Research 3 quick ways a small studio can use AI agents to save admin time. Give me a Doc with a heading and 3 bullet points each. Cite sources.
   ```

2. Open the resulting Doc and check it against what you asked for: heading, three items, three bullets each, sources. Refine if a part is missing.
3. Now an organisation task on email. Ask the agent to propose labels for your unread mail — proposing, not applying, so you review first.

   ```bash
   Suggest a label for each of my unread emails from this week: Client, Supplier, Internal or Newsletter. List them; do not apply labels yet.
   ```

4. Review the proposed labels. Approve only the ones you agree with, then let the agent apply just those.
5. Run a Drive organisation task. Ask the agent to propose a folder structure for a set of files, without moving anything yet.

   ```bash
   Look at the files in my 'Brightwave/Incoming' folder and propose a folder structure to organise them. Show the plan; do not move files yet.
   ```

6. Read the proposed structure. Adjust one folder name, then approve the move for a small, safe subset of files.
7. Confirm in Drive that only the files you approved were moved, and nothing else changed.
8. Note which of these two tasks you would want to run regularly — you will schedule one in Topic 3.

**Test it**

You have a research Doc in exactly the format you specified, labels applied only to the emails you approved, and a small set of files moved into an approved folder structure with nothing else changed.

> **Note:** Full commands and screenshots are in labs/lab-04-*.md. Use only accounts and data you are authorised to use. Never paste real passwords, API keys or confidential personal data into an agent instruction; use the supplied sample data if in doubt.

---


### Lab 5 — Automate Email — Inbox Summaries and Reply Drafting

Learning outcome: Produce a prioritised inbox summary and have the agent draft replies in your voice for approval..

Goal: This is the automation most people feel first: a clear inbox. The agent reads your mail and hands you a prioritised digest, then drafts replies to the messages that need one — in your voice, left as drafts for you to review and send. BUILDING BLOCK — the automation you build in this lab is added to your AI operations assistant, the connected toolkit you assemble across all 12 labs.

**What you'll build**

A prioritised inbox digest and two review-ready reply drafts in your voice.   (Tools: Inbox summary, prioritisation, reply drafting, tone matching, Gmail drafts, approvals.)

**Step-by-step**

1. Ask for a prioritised inbox summary with a clear structure so you can act on it in seconds.

   ```bash
   Summarise my unread emails from today. Group as: Urgent, Needs a reply, FYI. One line each with sender and the ask.
   ```

2. Read the digest and sanity-check it: is anything urgent mis-sorted? If so, refine the instruction (e.g. define what 'urgent' means to you).
3. Give the agent your tone so drafts sound like you. Describe it in a sentence and give one short example of how you sign off.

   ```bash
   My email tone: warm, brief, plain English. I open with 'Hi <name>,' and sign off 'Thanks, <YOUR NAME>'.
   ```

4. Ask the agent to draft replies to the two emails from your 'Needs a reply' group — as drafts only, not sent.

   ```bash
   Draft replies to the 2 'Needs a reply' emails using my tone. Save as drafts. Do not send.
   ```

5. Open each draft in Gmail. Check the facts, the tone and that it answered the actual ask. Edit anything that is not quite right.
6. Approve and send only the drafts you are happy with; leave the rest as drafts to finish later.
7. Refine your tone instruction once based on what you had to edit, so the next drafts need less correction.
8. Confirm in Gmail Sent that only the replies you approved were sent, and the digest matched your real inbox.

**Test it**

You produced a prioritised digest that matches your inbox, two drafts written in your voice, and sent only the ones you personally reviewed and approved.

> **Note:** Full commands and screenshots are in labs/lab-05-*.md. Use only accounts and data you are authorised to use. Never paste real passwords, API keys or confidential personal data into an agent instruction; use the supplied sample data if in doubt.

---


### Lab 6 — Work with Docs, Sheets and Slides — Generate, Review and Refine

Learning outcome: Have the agent create a Doc, populate a Sheet and draft a Slides deck, then review and refine each output..

Goal: Spark can produce first drafts across the Workspace apps so you start from 80%, not a blank page. You generate a document, turn scattered notes into a structured spreadsheet, and draft a short deck — then apply the review-and-refine discipline to each so the output is actually usable. BUILDING BLOCK — the automation you build in this lab is added to your AI operations assistant, the connected toolkit you assemble across all 12 labs.

**What you'll build**

A drafted Doc, a populated Sheet and a short Slides deck, each reviewed and refined once.   (Tools: Google Docs, Google Sheets, Google Slides, content generation, structured extraction, review and refine.)

**Step-by-step**

1. Generate a Doc from a brief. Be specific about structure and length so it is easy to review.

   ```bash
   Write a 1-page Brightwave client onboarding checklist in a Doc: sections for Kickoff, Access, Brand assets, Timeline. Use checkboxes.
   ```

2. Review the Doc against the brief. Refine one section that is thin, then accept the version you are happy with.
3. Populate a Sheet from unstructured input. Give the agent a few lines of notes and a target column layout.

   ```bash
   Turn these notes into a Sheet with columns Client, Contact, Service, Fee, Status: <paste 4-5 lines of your own notes or the Brightwave sample>.
   ```

4. Open the Sheet and check every row parsed into the right column. Fix the instruction and re-run if a column is misaligned.
5. Draft a Slides deck from the Doc you made. Keep it short so review is quick.

   ```bash
   Create a 5-slide deck from my onboarding checklist Doc: title slide plus one slide per section, 3 bullets each.
   ```

6. Review the deck: is each slide on-message and uncluttered? Refine one slide, then keep the improved version.
7. Reflect on the pattern you just used three times — generate, review, refine — and note where it saved you the most time.
8. Save the Doc, Sheet and deck into your Brightwave assistant's Drive folder so later workflows can reuse them.

**Test it**

You have a Doc, a Sheet and a Slides deck the agent generated, each reviewed and refined at least once, with the Sheet's data correctly placed in the right columns.

> **Note:** Full commands and screenshots are in labs/lab-06-*.md. Use only accounts and data you are authorised to use. Never paste real passwords, API keys or confidential personal data into an agent instruction; use the supplied sample data if in doubt.

---


## Topic 03 — Building Reusable Skills and Schedules  (25%)

Custom reusable skills · Schedules and triggers · Chaining workflows · Personalising behaviour

**Key concepts**

- Reusable skills — save a proven instruction as a named skill you can run again and again without re-typing it.
- The Ghostwriter skill — a worked example: a skill that drafts content in a consistent, personalised style on demand.
- Schedules — set an agent to run on a cadence, such as a digest every weekday morning, with no manual trigger.
- Conditional triggers — run a skill only when a condition is met, such as a new email from a specific sender.
- Chaining — connect skills so the output of one becomes the input of the next, forming a multi-step workflow.
- Personalisation — teach the agent your preferences, tone and recurring context so its output needs less editing.
- Style and voice — capture how you write once, and have every draft match it automatically.
- Skill hygiene — name, describe and test each skill so you and your team know exactly what it does.


### Lab 7 — Create a Custom Reusable Skill — the Ghostwriter

Learning outcome: Turn a proven instruction into a named, reusable skill and run it repeatedly with different inputs..

Goal: A skill is a saved instruction you can run again and again. You build the classic example — a Ghostwriter that drafts content in a consistent style — by capturing your best instruction, naming it, describing it, and testing it on two different inputs so you know it is reliable. BUILDING BLOCK — the automation you build in this lab is added to your AI operations assistant, the connected toolkit you assemble across all 12 labs.

**What you'll build**

A saved, named 'Brightwave Ghostwriter' skill, tested on two different inputs.   (Tools: Reusable skills, saving instructions, naming and describing, style capture, testing.)

**Step-by-step**

1. Start from a strong instruction. Write one that drafts a short piece of content in your studio's voice.

   ```bash
   Draft a 120-word LinkedIn post about <TOPIC> in Brightwave's voice: friendly, concrete, no hype, one clear call to action.
   ```

2. Run it once and refine until the style is right — this becomes the body of your skill.
3. Save it as a reusable skill. Give it a clear name and a one-line description of what it does and when to use it.

   ```bash
   Name: Brightwave Ghostwriter | Description: Drafts a short social post in Brightwave's voice from a topic.
   ```

4. Make the input a placeholder so the skill is reusable: the topic should be something you supply each time you run it.
5. Test the skill on a first topic. Check the draft matches the voice and the word count.
6. Run the SAME skill on a second, different topic. Confirm it stays in voice without you re-typing the instruction.
7. Add one guardrail to the skill's instruction: never invent statistics or client names; leave a placeholder instead.
8. Note two other repeatable tasks in your week that would make good skills — you will need candidates for chaining in Lab 9.

**Test it**

You can run your saved Ghostwriter skill by name on any topic and get an in-voice draft of the right length, without re-typing the instruction, and it never invents facts.

> **Note:** Full commands and screenshots are in labs/lab-07-*.md. Use only accounts and data you are authorised to use. Never paste real passwords, API keys or confidential personal data into an agent instruction; use the supplied sample data if in doubt.

---


### Lab 8 — Design Schedules and Conditional Triggers

Learning outcome: Schedule a skill to run automatically on a cadence and add a trigger that runs only when a condition is met..

Goal: Automation earns its keep when it runs without you. You put your inbox digest on a schedule so it arrives every weekday morning, then add a conditional trigger so a skill fires only when something specific happens — such as an email from a key client. BUILDING BLOCK — the automation you build in this lab is added to your AI operations assistant, the connected toolkit you assemble across all 12 labs.

**What you'll build**

A scheduled daily inbox digest and one conditional trigger, both tested.   (Tools: Schedules, cadence, conditional triggers, event conditions, approvals on automation.)

**Step-by-step**

1. Take your inbox-summary instruction from Lab 5 and set it to run on a schedule.

   ```bash
   Every weekday at 8:00am, summarise my unread emails as Urgent / Needs a reply / FYI and put the digest in a Doc named 'Daily Digest'.
   ```

2. Choose the cadence and time deliberately — early enough to be useful, not so early the inbox is empty.
3. Decide the approval posture for scheduled runs: reading and drafting can run unattended; sending or sharing should still need approval. Set it.
4. Test the schedule without waiting a day: use the 'run now' option to fire it once and confirm the digest Doc is created.
5. Now build a conditional trigger. Choose a condition that matters and a safe action (draft, don't send).

   ```bash
   When a new email arrives from <KEY CLIENT EMAIL>, draft a holding reply saying we'll respond within one business day. Save as draft; do not send.
   ```

6. Test the trigger safely: send yourself a test email that meets the condition (or use the sample), and confirm the draft is created.
7. Check the activity log to see the scheduled run and the triggered run recorded as separate entries.
8. Set a stop rule: note how you would pause or delete a schedule or trigger if it ever misbehaves.

**Test it**

Your inbox digest runs on its schedule (verified with 'run now') and your conditional trigger creates a draft only when the condition is met — both visible as entries in the activity log.

> **Note:** Full commands and screenshots are in labs/lab-08-*.md. Use only accounts and data you are authorised to use. Never paste real passwords, API keys or confidential personal data into an agent instruction; use the supplied sample data if in doubt.

---


### Lab 9 — Chain Multi-Step Workflows and Personalise Your Agent

Learning outcome: Connect skills so one feeds the next into a single workflow, and personalise the agent so output needs less editing..

Goal: Real automation is more than one step. You chain skills so the output of one becomes the input of the next — turning several manual actions into one run — and you personalise the agent with your recurring context and preferences so every result starts closer to done. BUILDING BLOCK — the automation you build in this lab is added to your AI operations assistant, the connected toolkit you assemble across all 12 labs.

**What you'll build**

A two-or-three-step chained workflow and a saved personalisation profile for your agent.   (Tools: Chaining, multi-step workflows, passing outputs as inputs, personalisation, preferences, style profile.)

**Step-by-step**

1. Sketch a short chain on paper first: step 1 produces something step 2 uses. Keep it to two or three steps.

   ```bash
   CHAIN: 1) summarise this week's client emails -> 2) draft a weekly update from that summary -> 3) create a Doc for review.
   ```

2. Build step 1 as an instruction (or reuse a skill) that produces a clear, structured output for the next step to consume.
3. Build step 2 so it explicitly takes step 1's output as its input, rather than starting from scratch.
4. Add step 3 to place the final result where you want it (a Doc in your Brightwave folder), as a draft for review.
5. Run the whole chain once and review each hand-off: did step 2 actually use step 1's output? Refine the weak link.
6. Now personalise the agent. Save a profile of recurring context so you stop repeating yourself.

   ```bash
   Remember: I'm the ops coordinator at Brightwave Studio. Our clients are SMEs. Default tone: warm and brief. Working hours 9-6, Mon-Fri.
   ```

7. Re-run one earlier task and confirm the personalisation improved it — less context to type, output closer to your style.
8. Save the chained workflow so you can run the whole thing next week with one instruction.

**Test it**

Running your chained workflow once produces the final Doc with each step visibly using the previous step's output, and your saved personalisation profile measurably reduces how much you have to edit or re-explain.

> **Note:** Full commands and screenshots are in labs/lab-09-*.md. Use only accounts and data you are authorised to use. Never paste real passwords, API keys or confidential personal data into an agent instruction; use the supplied sample data if in doubt.

---


## Topic 04 — Advanced Agentic Workflows and Real-World Automation  (20%)

Lead, expense and planning automation · Multi-app coordination · Guardrails · Monitoring and scaling

**Key concepts**

- Real-world automation — assemble skills and schedules into workflows that handle everyday business tasks end to end.
- Lead management — capture an enquiry, log it to a sheet and draft a timely follow-up, all through the agent.
- Expense and planning — turn receipts and notes into a tidy record, and a rough plan into a scheduled agenda.
- Multi-app coordination — a single workflow that spans Gmail, Calendar, Drive and Sheets in one connected run.
- Guardrails — set explicit limits on what an agent may do, so automation is safe by design, not by luck.
- Permissions and privacy — grant least access, keep confidential data out of prompts, and know where data flows.
- Monitoring — read the activity log to catch mistakes early and confirm your agents are doing the right thing.
- Improving and scaling — refine instructions, add guardrails and roll trusted agents out to more of your work or team.


### Lab 10 — Automate Lead Management, Expenses and Planning

Learning outcome: Build agent workflows that capture leads, log expenses and turn notes into a plan — end to end..

Goal: This is the payoff: automations that handle whole tasks. You build a lead-intake flow that logs an enquiry and drafts a follow-up, an expense flow that turns receipts and notes into a clean record, and a planning flow that turns rough notes into a scheduled agenda. BUILDING BLOCK — the automation you build in this lab is added to your AI operations assistant, the connected toolkit you assemble across all 12 labs.

**What you'll build**

Three real-world automations: lead intake, expense logging and a planning agenda — each tested once.   (Tools: Lead management, Sheets logging, follow-up drafting, expense extraction, planning, Calendar.)

**Step-by-step**

1. Build the lead-intake flow. From an enquiry email, log the lead to a Sheet and draft a follow-up for approval.

   ```bash
   From new emails labelled 'Lead', add a row to 'Leads' Sheet (Name, Company, Ask, Date) and draft a follow-up reply. Save drafts; do not send.
   ```

2. Test it with one sample enquiry. Confirm the row appears with the right fields and a sensible follow-up draft is created.
3. Build the expense flow. Turn a set of expense notes (or receipt details you type) into a clean, categorised record.

   ```bash
   Turn these expense notes into an 'Expenses' Sheet with Date, Vendor, Category, Amount, and a running total: <paste your notes or the sample>.
   ```

4. Review the expense Sheet: are categories sensible and the total correct? Refine the categories in the instruction and re-run if needed.
5. Build the planning flow. Turn rough notes about a piece of work into a sequenced plan with dates.

   ```bash
   Turn these notes into a step-by-step plan with suggested dates this month, then draft calendar events for each step. Do not create events yet.
   ```

6. Review the proposed plan and events. Approve creating events only for the steps you agree with, then check Calendar.
7. Look across the three flows and note where they share data (a lead could become a planned piece of work) — a hint for Lab 11.
8. Save all three as skills so they are ready to run again and to combine next.

**Test it**

You have a lead logged to a Sheet with an approved follow-up draft, an accurate categorised expense record with a correct total, and a plan whose approved steps appear as Calendar events.

> **Note:** Full commands and screenshots are in labs/lab-10-*.md. Use only accounts and data you are authorised to use. Never paste real passwords, API keys or confidential personal data into an agent instruction; use the supplied sample data if in doubt.

---


### Lab 11 — Coordinate Multi-App Workflows and Set Safe-Automation Guardrails

Learning outcome: Run one workflow that spans several Workspace apps, and set permission, privacy and safety guardrails..

Goal: Now the apps work together. You build a single workflow that touches Gmail, Sheets, Calendar and Drive in one run, then do the essential engineering work of safe automation: set least-privilege permissions, keep confidential data out of prompts, and write explicit guardrails. BUILDING BLOCK — the automation you build in this lab is added to your AI operations assistant, the connected toolkit you assemble across all 12 labs.

**What you'll build**

One multi-app workflow plus a written guardrails checklist applied to your agents.   (Tools: Multi-app coordination, Gmail, Sheets, Calendar, Drive, least privilege, privacy, guardrails.)

**Step-by-step**

1. Design a workflow that deliberately spans apps. Reuse skills from Lab 10 so this is coordination, not new work.

   ```bash
   When a 'Lead' email arrives: 1) log it to the Leads Sheet, 2) draft a follow-up, 3) add a 'Review lead' event tomorrow, 4) file the email to Drive/Leads.
   ```

2. Run it once on a sample lead and check each app in turn: Sheet row, Gmail draft, Calendar event, Drive file. Fix the step that failed.
3. Review permissions with least privilege in mind: does any agent have access it does not need? Remove access that is not required.
4. Set a privacy guardrail: instruct your agents never to include confidential data in outputs and to use placeholders for anything sensitive.

   ```bash
   Never put client financials, personal ID numbers or passwords into any draft, Sheet or Doc. Use <REDACTED> instead and flag it to me.
   ```

5. Set an action guardrail: nothing is sent, shared externally or deleted without explicit approval, even on scheduled runs.
6. Test a guardrail on purpose: ask the agent to do something the guardrail forbids and confirm it refuses or asks first.
7. Write a short guardrails checklist (permissions, privacy, actions, approvals) and apply it to every skill you keep.
8. Confirm in the activity log that the multi-app run is recorded as one connected workflow you can review end to end.

**Test it**

Your multi-app workflow completes across Gmail, Sheets, Calendar and Drive from a single trigger, your agent refuses a forbidden action when tested, and you have a written guardrails checklist applied to your kept skills.

> **Note:** Full commands and screenshots are in labs/lab-11-*.md. Use only accounts and data you are authorised to use. Never paste real passwords, API keys or confidential personal data into an agent instruction; use the supplied sample data if in doubt.

---


### Lab 12 — Monitor, Improve and Scale Your AI Agents

Learning outcome: Consolidate your assistant, monitor it from the activity log, improve weak instructions and plan to scale safely..

Goal: You finish by turning a set of automations into a dependable assistant. You review everything you built from the activity log, fix the instructions that produced weak results, and write a simple plan to scale your agents to more of your work — or your team — without losing control. BUILDING BLOCK — the automation you build in this lab is added to your AI operations assistant, the connected toolkit you assemble across all 12 labs.

**What you'll build**

A monitored, improved AI operations assistant and a one-page plan to scale it responsibly.   (Tools: Monitoring, activity log review, instruction improvement, reliability, scaling, governance.)

**Step-by-step**

1. Inventory your assistant: list every task, skill, schedule and workflow you built across the 12 labs.
2. Monitor from the activity log: review recent runs and mark any that produced a wrong, incomplete or off-tone result.
3. For each weak result, find the root cause in the instruction — usually a missing Input, Output or Limit — and fix it.

   ```bash
   Improve one skill: add the missing part (e.g. 'Output: a Doc named X' or 'Limit: never send') and re-run to confirm it is fixed.
   ```

4. Add a reliability check to your most-used skill: a line that makes the agent state what it did so you can verify at a glance.
5. Decide what is safe to run unattended and what must always pause for approval, and set each accordingly.
6. Write your scaling plan: which two automations to expand next, who else could use them, and the guardrails that must travel with them.
7. Pick one skill to hand over: document its name, purpose, inputs, output and guardrails so a colleague could run it safely.
8. Write your 30-day automation roadmap: one new automation a week, each with a 'Test it' check, starting with the highest time saver.

**Test it**

You have a written inventory of everything you built, at least one instruction improved after monitoring its log, a documented hand-over for one skill, and a one-page 30-day plan to scale your agents with guardrails.

> **Note:** Full commands and screenshots are in labs/lab-12-*.md. Use only accounts and data you are authorised to use. Never paste real passwords, API keys or confidential personal data into an agent instruction; use the supplied sample data if in doubt.

---


## Wrap-Up

You have built a connected set of AI agents across two days — from your first supervised task to scheduled, chained, guard-railed workflows that handle real work.

**What you built**

- Gemini Spark connected to Gmail, Calendar and Drive, with a tested first task.
- A toolkit of one-off tasks for research, inbox summaries, reply drafting and Docs/Sheets/Slides.
- A reusable Ghostwriter skill, a scheduled daily digest, a conditional trigger and a chained workflow.
- Real-world automations for leads, expenses and planning, coordinated across several Workspace apps.
- A set of guardrails, a monitoring habit and a plan to scale trusted agents to more of your work.

**What to do next**

- Point your best skills at a real, recurring task in your own week and measure the time saved.
- Review your agents' activity logs weekly and tighten any instruction that produced a wrong result.
- Share a proven skill with a colleague, with the guardrails documented.
- Add one new automation a week until your routine admin runs itself.

---


## Next Steps

- First pass: complete every lab yourself, following the steps and verifying each 'Test it' check.
- Second pass: rebuild your Ghostwriter skill, daily digest and a chained workflow from memory.
- Apply the techniques to a real recurring task in your own organisation, starting with guardrails.
- Review each lab's detailed steps in this guide and re-run the automations on your own Workspace.


## Glossary

- **AI agent** — Software that plans and carries out multi-step tasks toward a goal you set, not just a single reply.
- **Gemini Spark** — Google's agentic capability that acts across Workspace apps to complete tasks on your behalf.
- **Background agent** — An agent that works through a task while you do other things, reporting back when done.
- **Approval** — The step where Spark pauses and waits for you to authorise an action before it takes effect.
- **Activity log** — The record of every action an agent has taken, used to review, trust and undo its work.
- **Instruction** — A plain-language brief that states the goal, inputs, output and limits for an agent task.
- **Task** — A single instruction Spark runs, once, to produce a result you can review.
- **Skill** — A saved, named instruction you can reuse and run again without re-typing it.
- **Ghostwriter** — A worked example skill that drafts content in a consistent, personalised style.
- **Schedule** — A setting that runs an agent automatically on a cadence, such as every weekday morning.
- **Conditional trigger** — A rule that runs a skill only when a stated condition occurs, such as a new email from a sender.
- **Chaining** — Connecting skills so the output of one becomes the input of the next in a multi-step workflow.
- **Guardrail** — An explicit limit on what an agent may do, set so that automation is safe by design.
- **Least privilege** — Granting an agent only the access it needs for the task and no more.
- **Workspace** — Google's suite of Gmail, Calendar, Drive, Docs, Sheets and Slides that Spark acts within.
