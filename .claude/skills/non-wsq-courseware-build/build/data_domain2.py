"""
Domain 2 — Automating Work with Gemini Spark Tasks. Labs 4-6.

You now put the agent to work on real daily tasks: research and organisation,
email summaries and drafting, and generating content across Docs, Sheets and
Slides — always reviewing and refining the result. Each lab adds another task to
your Brightwave AI operations assistant.
"""

PROJECT_NOTE = (
 "BUILDING BLOCK — the automation you build in this lab is added to your AI "
 "operations assistant, the connected toolkit you assemble across all 12 labs."
)

DOMAIN2 = [
 dict(
 num=4, topic=2,
 title="Create One-Off Tasks for Research and Organisation",
 objective="Use one-off agent tasks to research a topic and to organise emails and Drive files.",
 desc="One-off tasks are the workhorse of Spark: a single instruction the agent runs once. You run a "
 "research task that returns a structured, reusable result, then an organisation task that tidies "
 "your inbox and Drive — reviewing both before you accept them. " + PROJECT_NOTE,
 build="A structured research brief in a Doc, plus a tidied inbox and a proposed Drive folder structure.",
 services="One-off tasks, research, summarisation, Gmail labels, Drive organisation, Docs",
 steps=[
 ("Run a research task with a clear output format. Ask for a short, structured brief you can reuse, not a wall of text.",
  "Research 3 quick ways a small studio can use AI agents to save admin time. Give me a Doc with a heading and 3 bullet points each. Cite sources."),
 ("Open the resulting Doc and check it against what you asked for: heading, three items, three bullets each, sources. Refine if a part is missing.", ""),
 ("Now an organisation task on email. Ask the agent to propose labels for your unread mail — proposing, not applying, so you review first.",
  "Suggest a label for each of my unread emails from this week: Client, Supplier, Internal or Newsletter. List them; do not apply labels yet."),
 ("Review the proposed labels. Approve only the ones you agree with, then let the agent apply just those.", ""),
 ("Run a Drive organisation task. Ask the agent to propose a folder structure for a set of files, without moving anything yet.",
  "Look at the files in my 'Brightwave/Incoming' folder and propose a folder structure to organise them. Show the plan; do not move files yet."),
 ("Read the proposed structure. Adjust one folder name, then approve the move for a small, safe subset of files.", ""),
 ("Confirm in Drive that only the files you approved were moved, and nothing else changed.", ""),
 ("Note which of these two tasks you would want to run regularly — you will schedule one in Topic 3.", ""),
 ],
 test="You have a research Doc in exactly the format you specified, labels applied only to the emails you approved, and a small set of files moved into an approved folder structure with nothing else changed.",
 ),
 dict(
 num=5, topic=2,
 title="Automate Email — Inbox Summaries and Reply Drafting",
 objective="Produce a prioritised inbox summary and have the agent draft replies in your voice for approval.",
 desc="This is the automation most people feel first: a clear inbox. The agent reads your mail and hands "
 "you a prioritised digest, then drafts replies to the messages that need one — in your voice, left "
 "as drafts for you to review and send. " + PROJECT_NOTE,
 build="A prioritised inbox digest and two review-ready reply drafts in your voice.",
 services="Inbox summary, prioritisation, reply drafting, tone matching, Gmail drafts, approvals",
 steps=[
 ("Ask for a prioritised inbox summary with a clear structure so you can act on it in seconds.",
  "Summarise my unread emails from today. Group as: Urgent, Needs a reply, FYI. One line each with sender and the ask."),
 ("Read the digest and sanity-check it: is anything urgent mis-sorted? If so, refine the instruction (e.g. define what 'urgent' means to you).", ""),
 ("Give the agent your tone so drafts sound like you. Describe it in a sentence and give one short example of how you sign off.",
  "My email tone: warm, brief, plain English. I open with 'Hi <name>,' and sign off 'Thanks, <YOUR NAME>'."),
 ("Ask the agent to draft replies to the two emails from your 'Needs a reply' group — as drafts only, not sent.",
  "Draft replies to the 2 'Needs a reply' emails using my tone. Save as drafts. Do not send."),
 ("Open each draft in Gmail. Check the facts, the tone and that it answered the actual ask. Edit anything that is not quite right.", ""),
 ("Approve and send only the drafts you are happy with; leave the rest as drafts to finish later.", ""),
 ("Refine your tone instruction once based on what you had to edit, so the next drafts need less correction.", ""),
 ("Confirm in Gmail Sent that only the replies you approved were sent, and the digest matched your real inbox.", ""),
 ],
 test="You produced a prioritised digest that matches your inbox, two drafts written in your voice, and sent only the ones you personally reviewed and approved.",
 ),
 dict(
 num=6, topic=2,
 title="Work with Docs, Sheets and Slides — Generate, Review and Refine",
 objective="Have the agent create a Doc, populate a Sheet and draft a Slides deck, then review and refine each output.",
 desc="Spark can produce first drafts across the Workspace apps so you start from 80%, not a blank page. "
 "You generate a document, turn scattered notes into a structured spreadsheet, and draft a short "
 "deck — then apply the review-and-refine discipline to each so the output is actually usable. " + PROJECT_NOTE,
 build="A drafted Doc, a populated Sheet and a short Slides deck, each reviewed and refined once.",
 services="Google Docs, Google Sheets, Google Slides, content generation, structured extraction, review and refine",
 steps=[
 ("Generate a Doc from a brief. Be specific about structure and length so it is easy to review.",
  "Write a 1-page Brightwave client onboarding checklist in a Doc: sections for Kickoff, Access, Brand assets, Timeline. Use checkboxes."),
 ("Review the Doc against the brief. Refine one section that is thin, then accept the version you are happy with.", ""),
 ("Populate a Sheet from unstructured input. Give the agent a few lines of notes and a target column layout.",
  "Turn these notes into a Sheet with columns Client, Contact, Service, Fee, Status: <paste 4-5 lines of your own notes or the Brightwave sample>."),
 ("Open the Sheet and check every row parsed into the right column. Fix the instruction and re-run if a column is misaligned.", ""),
 ("Draft a Slides deck from the Doc you made. Keep it short so review is quick.",
  "Create a 5-slide deck from my onboarding checklist Doc: title slide plus one slide per section, 3 bullets each."),
 ("Review the deck: is each slide on-message and uncluttered? Refine one slide, then keep the improved version.", ""),
 ("Reflect on the pattern you just used three times — generate, review, refine — and note where it saved you the most time.", ""),
 ("Save the Doc, Sheet and deck into your Brightwave assistant's Drive folder so later workflows can reuse them.", ""),
 ],
 test="You have a Doc, a Sheet and a Slides deck the agent generated, each reviewed and refined at least once, with the Sheet's data correctly placed in the right columns.",
 ),
]
