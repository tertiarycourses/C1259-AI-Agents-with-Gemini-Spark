"""
Domain 3 — Building Reusable Skills and Schedules. Labs 7-9.

You stop re-typing instructions and start building automation that lasts: save a
proven instruction as a named, reusable skill; make it run on a schedule or when
a condition is met; chain skills into a multi-step workflow; and personalise the
agent so its output needs less editing. Each lab adds durable automation to your
Brightwave AI operations assistant.
"""

PROJECT_NOTE = (
 "BUILDING BLOCK — the automation you build in this lab is added to your AI "
 "operations assistant, the connected toolkit you assemble across all 12 labs."
)

DOMAIN3 = [
 dict(
 num=7, topic=3,
 title="Create a Custom Reusable Skill — the Ghostwriter",
 objective="Turn a proven instruction into a named, reusable skill and run it repeatedly with different inputs.",
 desc="A skill is a saved instruction you can run again and again. You build the classic example — a "
 "Ghostwriter that drafts content in a consistent style — by capturing your best instruction, naming "
 "it, describing it, and testing it on two different inputs so you know it is reliable. " + PROJECT_NOTE,
 build="A saved, named 'Brightwave Ghostwriter' skill, tested on two different inputs.",
 services="Reusable skills, saving instructions, naming and describing, style capture, testing",
 steps=[
 ("Start from a strong instruction. Write one that drafts a short piece of content in your studio's voice.",
  "Draft a 120-word LinkedIn post about <TOPIC> in Brightwave's voice: friendly, concrete, no hype, one clear call to action."),
 ("Run it once and refine until the style is right — this becomes the body of your skill.", ""),
 ("Save it as a reusable skill. Give it a clear name and a one-line description of what it does and when to use it.",
  "Name: Brightwave Ghostwriter | Description: Drafts a short social post in Brightwave's voice from a topic."),
 ("Make the input a placeholder so the skill is reusable: the topic should be something you supply each time you run it.", ""),
 ("Test the skill on a first topic. Check the draft matches the voice and the word count.", ""),
 ("Run the SAME skill on a second, different topic. Confirm it stays in voice without you re-typing the instruction.", ""),
 ("Add one guardrail to the skill's instruction: never invent statistics or client names; leave a placeholder instead.", ""),
 ("Note two other repeatable tasks in your week that would make good skills — you will need candidates for chaining in Lab 9.", ""),
 ],
 test="You can run your saved Ghostwriter skill by name on any topic and get an in-voice draft of the right length, without re-typing the instruction, and it never invents facts.",
 ),
 dict(
 num=8, topic=3,
 title="Design Schedules and Conditional Triggers",
 objective="Schedule a skill to run automatically on a cadence and add a trigger that runs only when a condition is met.",
 desc="Automation earns its keep when it runs without you. You put your inbox digest on a schedule so it "
 "arrives every weekday morning, then add a conditional trigger so a skill fires only when something "
 "specific happens — such as an email from a key client. " + PROJECT_NOTE,
 build="A scheduled daily inbox digest and one conditional trigger, both tested.",
 services="Schedules, cadence, conditional triggers, event conditions, approvals on automation",
 steps=[
 ("Take your inbox-summary instruction from Lab 5 and set it to run on a schedule.",
  "Every weekday at 8:00am, summarise my unread emails as Urgent / Needs a reply / FYI and put the digest in a Doc named 'Daily Digest'."),
 ("Choose the cadence and time deliberately — early enough to be useful, not so early the inbox is empty.", ""),
 ("Decide the approval posture for scheduled runs: reading and drafting can run unattended; sending or sharing should still need approval. Set it.", ""),
 ("Test the schedule without waiting a day: use the 'run now' option to fire it once and confirm the digest Doc is created.", ""),
 ("Now build a conditional trigger. Choose a condition that matters and a safe action (draft, don't send).",
  "When a new email arrives from <KEY CLIENT EMAIL>, draft a holding reply saying we'll respond within one business day. Save as draft; do not send."),
 ("Test the trigger safely: send yourself a test email that meets the condition (or use the sample), and confirm the draft is created.", ""),
 ("Check the activity log to see the scheduled run and the triggered run recorded as separate entries.", ""),
 ("Set a stop rule: note how you would pause or delete a schedule or trigger if it ever misbehaves.", ""),
 ],
 test="Your inbox digest runs on its schedule (verified with 'run now') and your conditional trigger creates a draft only when the condition is met — both visible as entries in the activity log.",
 ),
 dict(
 num=9, topic=3,
 title="Chain Multi-Step Workflows and Personalise Your Agent",
 objective="Connect skills so one feeds the next into a single workflow, and personalise the agent so output needs less editing.",
 desc="Real automation is more than one step. You chain skills so the output of one becomes the input of "
 "the next — turning several manual actions into one run — and you personalise the agent with your "
 "recurring context and preferences so every result starts closer to done. " + PROJECT_NOTE,
 build="A two-or-three-step chained workflow and a saved personalisation profile for your agent.",
 services="Chaining, multi-step workflows, passing outputs as inputs, personalisation, preferences, style profile",
 steps=[
 ("Sketch a short chain on paper first: step 1 produces something step 2 uses. Keep it to two or three steps.",
  "CHAIN: 1) summarise this week's client emails -> 2) draft a weekly update from that summary -> 3) create a Doc for review."),
 ("Build step 1 as an instruction (or reuse a skill) that produces a clear, structured output for the next step to consume.", ""),
 ("Build step 2 so it explicitly takes step 1's output as its input, rather than starting from scratch.", ""),
 ("Add step 3 to place the final result where you want it (a Doc in your Brightwave folder), as a draft for review.", ""),
 ("Run the whole chain once and review each hand-off: did step 2 actually use step 1's output? Refine the weak link.", ""),
 ("Now personalise the agent. Save a profile of recurring context so you stop repeating yourself.",
  "Remember: I'm the ops coordinator at Brightwave Studio. Our clients are SMEs. Default tone: warm and brief. Working hours 9-6, Mon-Fri."),
 ("Re-run one earlier task and confirm the personalisation improved it — less context to type, output closer to your style.", ""),
 ("Save the chained workflow so you can run the whole thing next week with one instruction.", ""),
 ],
 test="Running your chained workflow once produces the final Doc with each step visibly using the previous step's output, and your saved personalisation profile measurably reduces how much you have to edit or re-explain.",
 ),
]
