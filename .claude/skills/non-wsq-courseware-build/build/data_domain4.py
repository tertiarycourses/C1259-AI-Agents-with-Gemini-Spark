"""
Domain 4 — Advanced Agentic Workflows and Real-World Automation. Labs 10-12.

You bring everything together into workflows that handle real business tasks:
lead management, expenses and planning; coordinate a single workflow across
several Workspace apps; set the guardrails that make automation safe; and finish
by monitoring, improving and planning to scale your Brightwave AI operations
assistant responsibly.
"""

PROJECT_NOTE = (
 "BUILDING BLOCK — the automation you build in this lab is added to your AI "
 "operations assistant, the connected toolkit you assemble across all 12 labs."
)

DOMAIN4 = [
 dict(
 num=10, topic=4,
 title="Automate Lead Management, Expenses and Planning",
 objective="Build agent workflows that capture leads, log expenses and turn notes into a plan — end to end.",
 desc="This is the payoff: automations that handle whole tasks. You build a lead-intake flow that logs an "
 "enquiry and drafts a follow-up, an expense flow that turns receipts and notes into a clean record, "
 "and a planning flow that turns rough notes into a scheduled agenda. " + PROJECT_NOTE,
 build="Three real-world automations: lead intake, expense logging and a planning agenda — each tested once.",
 services="Lead management, Sheets logging, follow-up drafting, expense extraction, planning, Calendar",
 steps=[
 ("Build the lead-intake flow. From an enquiry email, log the lead to a Sheet and draft a follow-up for approval.",
  "From new emails labelled 'Lead', add a row to 'Leads' Sheet (Name, Company, Ask, Date) and draft a follow-up reply. Save drafts; do not send."),
 ("Test it with one sample enquiry. Confirm the row appears with the right fields and a sensible follow-up draft is created.", ""),
 ("Build the expense flow. Turn a set of expense notes (or receipt details you type) into a clean, categorised record.",
  "Turn these expense notes into an 'Expenses' Sheet with Date, Vendor, Category, Amount, and a running total: <paste your notes or the sample>."),
 ("Review the expense Sheet: are categories sensible and the total correct? Refine the categories in the instruction and re-run if needed.", ""),
 ("Build the planning flow. Turn rough notes about a piece of work into a sequenced plan with dates.",
  "Turn these notes into a step-by-step plan with suggested dates this month, then draft calendar events for each step. Do not create events yet."),
 ("Review the proposed plan and events. Approve creating events only for the steps you agree with, then check Calendar.", ""),
 ("Look across the three flows and note where they share data (a lead could become a planned piece of work) — a hint for Lab 11.", ""),
 ("Save all three as skills so they are ready to run again and to combine next.", ""),
 ],
 test="You have a lead logged to a Sheet with an approved follow-up draft, an accurate categorised expense record with a correct total, and a plan whose approved steps appear as Calendar events.",
 ),
 dict(
 num=11, topic=4,
 title="Coordinate Multi-App Workflows and Set Safe-Automation Guardrails",
 objective="Run one workflow that spans several Workspace apps, and set permission, privacy and safety guardrails.",
 desc="Now the apps work together. You build a single workflow that touches Gmail, Sheets, Calendar and "
 "Drive in one run, then do the essential engineering work of safe automation: set least-privilege "
 "permissions, keep confidential data out of prompts, and write explicit guardrails. " + PROJECT_NOTE,
 build="One multi-app workflow plus a written guardrails checklist applied to your agents.",
 services="Multi-app coordination, Gmail, Sheets, Calendar, Drive, least privilege, privacy, guardrails",
 steps=[
 ("Design a workflow that deliberately spans apps. Reuse skills from Lab 10 so this is coordination, not new work.",
  "When a 'Lead' email arrives: 1) log it to the Leads Sheet, 2) draft a follow-up, 3) add a 'Review lead' event tomorrow, 4) file the email to Drive/Leads."),
 ("Run it once on a sample lead and check each app in turn: Sheet row, Gmail draft, Calendar event, Drive file. Fix the step that failed.", ""),
 ("Review permissions with least privilege in mind: does any agent have access it does not need? Remove access that is not required.", ""),
 ("Set a privacy guardrail: instruct your agents never to include confidential data in outputs and to use placeholders for anything sensitive.",
  "Never put client financials, personal ID numbers or passwords into any draft, Sheet or Doc. Use <REDACTED> instead and flag it to me."),
 ("Set an action guardrail: nothing is sent, shared externally or deleted without explicit approval, even on scheduled runs.", ""),
 ("Test a guardrail on purpose: ask the agent to do something the guardrail forbids and confirm it refuses or asks first.", ""),
 ("Write a short guardrails checklist (permissions, privacy, actions, approvals) and apply it to every skill you keep.", ""),
 ("Confirm in the activity log that the multi-app run is recorded as one connected workflow you can review end to end.", ""),
 ],
 test="Your multi-app workflow completes across Gmail, Sheets, Calendar and Drive from a single trigger, your agent refuses a forbidden action when tested, and you have a written guardrails checklist applied to your kept skills.",
 ),
 dict(
 num=12, topic=4,
 title="Monitor, Improve and Scale Your AI Agents",
 objective="Consolidate your assistant, monitor it from the activity log, improve weak instructions and plan to scale safely.",
 desc="You finish by turning a set of automations into a dependable assistant. You review everything you "
 "built from the activity log, fix the instructions that produced weak results, and write a simple "
 "plan to scale your agents to more of your work — or your team — without losing control. " + PROJECT_NOTE,
 build="A monitored, improved AI operations assistant and a one-page plan to scale it responsibly.",
 services="Monitoring, activity log review, instruction improvement, reliability, scaling, governance",
 steps=[
 ("Inventory your assistant: list every task, skill, schedule and workflow you built across the 12 labs.", ""),
 ("Monitor from the activity log: review recent runs and mark any that produced a wrong, incomplete or off-tone result.", ""),
 ("For each weak result, find the root cause in the instruction — usually a missing Input, Output or Limit — and fix it.",
  "Improve one skill: add the missing part (e.g. 'Output: a Doc named X' or 'Limit: never send') and re-run to confirm it is fixed."),
 ("Add a reliability check to your most-used skill: a line that makes the agent state what it did so you can verify at a glance.", ""),
 ("Decide what is safe to run unattended and what must always pause for approval, and set each accordingly.", ""),
 ("Write your scaling plan: which two automations to expand next, who else could use them, and the guardrails that must travel with them.", ""),
 ("Pick one skill to hand over: document its name, purpose, inputs, output and guardrails so a colleague could run it safely.", ""),
 ("Write your 30-day automation roadmap: one new automation a week, each with a 'Test it' check, starting with the highest time saver.", ""),
 ],
 test="You have a written inventory of everything you built, at least one instruction improved after monitoring its log, a documented hand-over for one skill, and a one-page 30-day plan to scale your agents with guardrails.",
 ),
]
