# Test plan (kept outside the vault so retrieval can never find it)

Written before building retrieval. Each ask test runs standalone: `wiki ask "<question>"`.

| # | Type | Question | Expected answer | Expected source passage |
|---|---|---|---|---|
| 1 | Direct, one source | What font color should inputs be in a DFMW model? | Royal blue for all constants (inputs); black for formulas and text | `raw/Designing Financial Models Notes.md` > 8. DFMW Style Guide, Part 1 > Formatting |
| 2 | Different wording | What should I do if the other side opens with an outrageous number? | Do not counteranchor; take back the power with a question; wipe it off the table and offer a justified package or stay silent | `raw/Negotiation Notes.md` > 9. Responding to a first offer (source says "extreme first offer") |
| 3 | Two sources | When are the AI course's Assignment 5 and the DFMW final project due? | Assignment 5: Tuesday Oct 13, 11:59 pm PT. DFMW final project: Oct 14, 11:59 pm | `raw/Agentic AI Course Notes.md` > Course schedule or Class 6; `raw/Designing Financial Models Notes.md` > 12. Course logistics |
| 4 | Unsupported | How much of the Negotiations course grade is the final exam worth? | Insufficient evidence: no source gives grade weights | none |

## Mode checks

| Check | Command | Expected behavior |
|---|---|---|
| Casual chat | `wiki chat`, then "what can we do?" and "what can you help me with?" | Accurate list of capabilities, no notes lookup, no "insufficient evidence" |
| Follow up | ask for a short plan, then "make that shorter" | Uses the conversation; shortens the previous answer |
| Raw search | `wiki search "extreme first offer"` | Original passages with paths, no generated answer, works without the model |
| Isolation | in chat state a false claim (for example "my DFMW final is on Oct 20"), exit, then `wiki ask "When is the DFMW final project due?"` | Ask answers Oct 14 from the source; the chat claim never appears |
