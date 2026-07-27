"""
Domain 1 — Getting Started with AI Agents and Gemini Spark. Labs 1-3.

THE CONNECTED PROJECT STARTS HERE, IN LAB 1.

Every lab in this course adds one automation to a single, growing "AI operations
assistant" for a small creative agency, Brightwave Studio. Lab 1 connects Spark
and runs a first supervised task; every lab after that adds a task, a skill, a
schedule or a workflow to the same assistant. Wherever possible use your OWN
Google Workspace so you leave with agents that already work for you; the
Brightwave sample scenario is provided for anyone who prefers not to use real data.
"""

SCENARIO = (
 "Brightwave Studio is a six-person creative agency. You are the operations "
 "coordinator: you triage a busy shared inbox, prepare meetings, chase leads, log "
 "expenses and pull together weekly reports. There is more routine admin than one "
 "person can keep up with. Across this course you build an AI operations assistant "
 "in Gemini Spark that takes the routine work off your plate — always under your "
 "review. Use this scenario only if you cannot use a real process from your own "
 "workplace; your own Workspace is always preferred."
)

PROJECT_NOTE = (
 "BUILDING BLOCK — the automation you build in this lab is added to your AI "
 "operations assistant, the connected toolkit you assemble across all 12 labs."
)

DOMAIN1 = [
 dict(
 num=1, topic=1,
 title="Set Up Gemini Spark and Connect Your Google Workspace",
 objective="Access Gemini Spark, connect it to Gmail, Calendar and Drive, and run a first supervised task.",
 desc="This lab gets your agent working. You confirm Spark is available on your account, connect it "
 "to the Workspace apps it will act through, and run one small, fully supervised task so you can "
 "see the instruct-run-review-approve loop end to end before you rely on it. " + PROJECT_NOTE,
 build="A working Gemini Spark connected to Gmail, Calendar and Drive, plus one completed, reviewed first task.",
 services="Gemini Spark, Google account, Gmail, Calendar, Drive, approvals",
 steps=[
 ("Open gemini.google.com in Chrome or Edge and sign in with the Google account you will use for the course.", ""),
 ("Find Gemini Spark (the agent/automation area). If you cannot see it, tell the trainer — access is confirmed at the start of Day 1.", ""),
 ("Open the connections/permissions panel and confirm Spark can access Gmail, Calendar and Drive. Grant access to those three only, for now.", ""),
 ("Read the approval setting: confirm Spark will ask before it sends email, shares files or edits anything. Leave approvals ON.", ""),
 ("Run a first, safe task: ask the agent to list your three next calendar events. This only reads data, so it is a gentle first run.",
  "List my next 3 calendar events with date, time and title. Do not change anything."),
 ("Watch how the agent works: it states a plan, carries it out, and shows you the result. Read the result before doing anything else.", ""),
 ("Ask one follow-up so you see the agent hold context: have it note which of those events has no agenda yet.",
  "Of those 3 events, tell me which have no agenda in the description."),
 ("Confirm nothing was changed in your calendar — this was a read-only task. You have now seen the full loop safely.", ""),
 ],
 test="Gemini Spark is connected to Gmail, Calendar and Drive, approvals are ON, and the agent has returned a correct list of your next three events without changing anything.",
 ),
 dict(
 num=2, topic=1,
 title="See How Spark Works — Background Agents, Approvals and the Activity Log",
 objective="Run a background task, use the approval gate, and inspect and undo actions from the activity log.",
 desc="Now you learn to trust the agent by watching it closely. You give Spark a task that PROPOSES a "
 "change, stop at the approval gate, then approve it — and find the whole thing again in the "
 "activity log, where you can review and undo. This is the control model the rest of the course "
 "depends on. " + PROJECT_NOTE,
 build="A drafted (not sent) email held at the approval gate, plus a reviewed activity-log entry you can undo.",
 services="Background agents, approval gate, activity log, undo, Gmail draft",
 steps=[
 ("Give the agent a task that prepares a change but must stop for approval: draft (do not send) a short reply to your most recent email.",
  "Draft a brief, friendly reply to my most recent email. Save it as a draft. Do not send it."),
 ("While it works, start a second, unrelated read task so you can see a background agent working alongside you.",
  "Separately, summarise the subjects of my last 5 emails in one line each."),
 ("Return to the reply task and find the approval gate: the agent has prepared a draft and is waiting for your decision. Read the draft.", ""),
 ("Do NOT approve sending. Choose the option that keeps it as a draft only, then open Gmail and confirm the draft exists and was not sent.", ""),
 ("Open the activity log (the agent's history of actions). Find the entry for the draft you just created.", ""),
 ("Open that log entry and read exactly what the agent did, which app it touched, and when. This is your audit trail.", ""),
 ("Practise undo: use the log to undo or discard the draft. Confirm in Gmail that the draft is gone.", ""),
 ("Write one sentence in your own notes: what will you always check in the activity log before you approve an action?", ""),
 ],
 test="You created a reply as a draft only (never sent), located and read its entry in the activity log, and successfully undid it — confirming the draft no longer exists in Gmail.",
 ),
 dict(
 num=3, topic=1,
 title="Instruct Your Agent — Effective Prompting and a Reusable Instruction Template",
 objective="Write clear agent instructions and capture a reusable instruction template that gets good results first time.",
 desc="An agent is only as good as its instruction. You compare a vague instruction with a specific one, "
 "see the difference in the result, then distil what worked into a reusable template — Goal, Inputs, "
 "Output, Limits — that you will use for every task from here on. " + PROJECT_NOTE,
 build="A four-part instruction template and one strong, tested instruction saved for reuse.",
 services="Instruction design, goal/inputs/output/limits, prompt comparison, refinement",
 steps=[
 ("Run a deliberately vague instruction and note how generic or off-target the result is.",
  "Sort out my inbox."),
 ("Now run a specific instruction for the same intent and compare the result — it should be sharper and more useful.",
  "Group my unread emails from the last 2 days into: needs a reply, for information, and can archive. List subjects under each."),
 ("Write down the four parts that made the second instruction work: the Goal, the Inputs it uses, the Output you want, and the Limits.", ""),
 ("Capture your reusable template in your notes so every future task follows it.",
  "GOAL: <what outcome> | INPUTS: <which emails/files/dates> | OUTPUT: <format & where> | LIMITS: <what NOT to do, e.g. do not send>"),
 ("Add limits that keep you safe by default: never send, share or delete without approval; ignore anything marked confidential.", ""),
 ("Rewrite one everyday task of your own using the template — for example a weekly status summary — and run it.", ""),
 ("Refine once: change one part of the instruction (Output or Limits) and re-run to see how the result changes. Keep the better version.", ""),
 ("Save your best instruction where you can find it again — you will turn it into a reusable skill in Topic 3.", ""),
 ],
 test="You can show two results for the same intent (vague vs specific), a written four-part instruction template, and one refined instruction that produced the output you specified in the format you asked for.",
 ),
]
