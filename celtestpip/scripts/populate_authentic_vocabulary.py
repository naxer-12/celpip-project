import os
import re
import glob

PAGES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "pages")

# Authentic CELPIP vocabulary bank tailored to each section
VOCAB_BANKS = {
    "reading-part-1-reading-correspondence": [
        ("correspondence", "noun", "written communication such as letters, emails, or memos", "All official correspondence must be conducted through company email."),
        ("inquiry", "noun", "an official or formal request for information", "We received your inquiry regarding our seasonal pricing discounts."),
        ("complimentary", "adjective", "given or provided free of charge as a courtesy", "Guests enjoy complimentary breakfast each morning."),
        ("accommodate", "verb", "to provide lodging, space, or make adjustments to suit needs", "The hotel upgraded our room to accommodate our large family."),
        ("inconvenience", "noun", "trouble or difficulty caused to someone", "We sincerely apologize for any inconvenience caused by the delay."),
        ("reimbursement", "noun", "repayment for expenses incurred", "Submit your receipts within 30 days for prompt reimbursement."),
        ("forthcoming", "adjective", "about to happen or appear in the near future", "Details about the forthcoming workshop will be emailed soon."),
        ("discrepancy", "noun", "a lack of compatibility or similarity between two facts", "The accountant noticed a discrepancy between the two invoices."),
        ("rectify", "verb", "to put right or correct an error", "Customer support acted quickly to rectify the billing error."),
        ("tentative", "adjective", "not certain or fixed; provisional", "We scheduled a tentative meeting for next Tuesday at 2 PM."),
        ("punctual", "adjective", "happening or doing something at the agreed time", "Participants are requested to be punctual for all sessions."),
        ("eligible", "adjective", "having the right for or meeting the conditions for something", "Only permanent residents are eligible to apply for this grant."),
        ("promptly", "adverb", "immediately and without delay", "Please respond promptly to confirm your attendance."),
        ("cordially", "adverb", "in a warm and friendly manner", "You are cordially invited to our annual community gala."),
        ("delegate", "verb", "to entrust a task or responsibility to another person", "Managers should delegate routine tasks to team members."),
        ("undertake", "verb", "to commit oneself to and begin an enterprise or responsibility", "Our department agreed to undertake the security review."),
        ("authorize", "verb", "to give official permission for or approval to", "Only the director can authorize expenditures over five hundred dollars."),
        ("confidential", "adjective", "intended to be kept secret", "Please treat all attached client records as strictly confidential."),
        ("amendment", "noun", "a minor change or addition designed to improve a text or piece of legislation", "Both parties signed the amendment to the lease agreement."),
        ("stipulate", "verb", "to demand or specify a requirement as part of an agreement", "The contract stipulates that rent is due on the first of each month."),
        ("accordance", "noun", "conformity or compliance with a rule or standard", "Work was completed in accordance with local safety standards."),
        ("supercede", "verb", "to take the place of a person or thing previously in authority or use", "The new handbook will supercede all previous workplace policies."),
        ("reciprocal", "adjective", "given, felt, or done in return", "The two universities established a reciprocal student exchange program."),
        ("obligatory", "adjective", "required by a legal, moral, or other rule; compulsory", "Attendance at the workplace safety orientation is obligatory."),
        ("terminate", "verb", "to bring to an end", "Either party may terminate the agreement with thirty days written notice."),
        ("formalize", "verb", "to give legal or official status to something", "The signing ceremony formalizes our partnership with the city council."),
        ("subsequent", "adjective", "coming after something in time; following", "Subsequent meetings will be held virtually rather than in person."),
        ("preceding", "adjective", "coming before something in order, position, or time", "Review the summary in the preceding chapter before continuing."),
        ("enclosure", "noun", "a document or item placed in an envelope with a letter", "Please sign and return the enclosure at your earliest convenience."),
        ("invoice", "noun", "a list of goods sent or services provided with a statement of the sum due", "Payment is due thirty days from the invoice date."),
        ("overdue", "adjective", "not having arrived, happened, or been done by the expected time", "Our records show that your quarterly membership fee is overdue."),
        ("settlement", "noun", "an official agreement intended to resolve a dispute", "Both parties reached a fair settlement outside of court."),
        ("arrears", "noun", "money that is owed and should have been paid earlier", "The tenant settled all rent arrears before moving out."),
        ("acknowledgment", "noun", "acceptance of the truth or existence of something, or a confirmation of receipt", "You will receive an email acknowledgment once your application is received."),
        ("consensus", "noun", "a general agreement among a group of people", "The committee reached a consensus on the new vacation schedule."),
        ("protocol", "noun", "the official procedure or system of rules governing affairs", "Staff must follow strict sanitary protocols in the laboratory."),
        ("memorandum", "noun", "a written message in business or diplomacy", "The CEO circulated an internal memorandum regarding holiday hours."),
        ("directive", "noun", "an official or authoritative instruction", "Health authorities issued a new directive on seasonal vaccinations."),
        ("feasibility", "noun", "the state or degree of being easily or conveniently done", "Engineers conducted a feasibility study on the transit line extension."),
        ("admissible", "adjective", "acceptable or valid, especially as evidence in a court or official setting", "Official receipts are the only admissible proof of payment."),
        ("grievance", "noun", "a real or imagined cause for complaint, especially unfair treatment", "Employees may submit a grievance to the human resources panel."),
        ("arbitration", "noun", "the use of an independent person or body to settle a dispute", "Disputes between management and the union were resolved through arbitration."),
        ("waiver", "noun", "an act or instance of waiving a right or claim", "All participants must sign a liability waiver before taking the tour."),
        ("statutory", "adjective", "required, permitted, or enacted by statute", "Full-time employees receive two weeks of statutory paid leave."),
        ("compliance", "noun", "the action or fact of complying with a wish or command", "Our building underwent an inspection to ensure safety compliance."),
        ("adherence", "noun", "attachment or commitment to a person, cause, or rule", "Strict adherence to speed limits is enforced across the school zone."),
        ("jurisdiction", "noun", "the official power to make legal decisions and judgments", "The municipal court has jurisdiction over local traffic violations."),
        ("tenancy", "noun", "possession of land or property as a tenant", "The agreement outlines terms for a twelve-month residential tenancy."),
        ("premises", "noun", "a house or building, together with its land and outbuildings", "Smoking is strictly prohibited anywhere on school premises."),
        ("itinerary", "noun", "a planned route or journey with scheduled dates and times", "The travel coordinator sent us our finalized conference itinerary."),
        ("reservation", "noun", "an arrangement to have something kept for someone's use", "We recommend making a dinner reservation well in advance."),
        ("clarification", "noun", "an explanation that makes something easier to understand", "Please contact us if you require further clarification on your bill."),
        ("acknowledge", "verb", "to accept or admit the existence or truth of, or confirm receipt", "We wish to acknowledge receipt of your formal complaint."),
        ("compensation", "noun", "something awarded to compensate for loss, suffering, or injury", "The airline provided food vouchers and hotel compensation for the delay."),
        ("schedule", "verb", "to arrange or plan an event for a particular time", "Please schedule your road test through the online portal."),
        ("postpone", "verb", "to cause or arrange for something to take place at a later time", "Bad weather forced organizers to postpone the outdoor concert."),
        ("confirmation", "noun", "the action of confirming something or the state of being confirmed", "Keep your booking confirmation handy when boarding the train."),
        ("cancellation", "noun", "the action of canceling something that had been arranged", "Cancellations made 24 hours in advance incur no penalty fees."),
        ("courtesy", "noun", "polite behavior or gestures extended to others", "As a courtesy, parking is free for hotel guests on weekends."),
        ("expedite", "verb", "to make an action or process happen sooner or be accomplished more quickly", "Pay an extra fee to expedite passport processing within three days."),
        ("sincerely", "adverb", "in a sincere or genuine way, used as a formal closing in letters", "I look forward to hearing from you soon. Sincerely, Jane Doe."),
        ("apprise", "verb", "to inform or tell someone about a situation", "Keep your manager apprised of any unexpected project delays."),
        ("designate", "verb", "to appoint someone or specify a place for a particular purpose", "Please park only in the designated visitor spaces."),
        ("liaison", "noun", "communication or cooperation that facilitates a close working relationship", "She serves as the community liaison between residents and city council."),
        ("remittance", "noun", "a sum of money sent in payment for goods or services", "Please mail your remittance to the address shown on the invoice."),
        ("concurrence", "noun", "agreement or consistency in opinion or decision", "The plan was approved with the full concurrence of all committee members."),
        ("indemnity", "noun", "security or protection against a loss or financial burden", "The contract includes an indemnity clause covering unexpected damages."),
        ("lessee", "noun", "a person who holds the lease of a property; a tenant", "The lessee is responsible for maintaining smoke detector batteries."),
        ("lessor", "noun", "a person who leases or lets property to another; a landlord", "The lessor agreed to replace the heating unit before winter."),
        ("provisional", "adjective", "arranged or existing for the present, possibly to be changed later", "She was granted a provisional driver's license pending the road test."),
        ("forthwith", "adverb", "immediately; without delay", "Violators must vacate the reserved premises forthwith."),
        ("hereunto", "adverb", "to this document, matter, or place", "The parties have hereunto set their hands and seals."),
        ("whereupon", "adverb", "immediately after which", "The inspector completed the review, whereupon operations resumed promptly."),
        ("notwithstanding", "preposition", "in spite of; despite", "Notwithstanding heavy snow, transit buses operated on a reduced schedule."),
        ("hereinafter", "adverb", "further on in this document", "The ABC Company, hereinafter referred to as the Employer, agrees to terms."),
        ("thereof", "adverb", "of the thing just mentioned", "Inspect the vehicle and report any damage thereof immediately."),
        ("heretofore", "adverb", "before now; previously", "Fees heretofore paid cannot be refunded once classes have commenced."),
        ("indispensable", "adjective", "absolutely necessary", "Reliable internet access has become indispensable for remote employees."),
        ("exemplary", "adjective", "serving as a desirable model; representing the best of its kind", "The attendant received praise for exemplary customer service."),
        ("reiterate", "verb", "to say something again or a number of times, typically for emphasis", "Let me reiterate that all deadlines are non-negotiable."),
        ("substantiate", "verb", "to provide evidence to support or prove the truth of", "Please provide payroll receipts to substantiate your claim."),
        ("discretionary", "adjective", "available for use at the discretion of the user", "Employees are given three discretionary personal days per year.")
    ]
}

# Generic rich fallback vocabulary bank for other bundles
GENERIC_CELPIP_VOCAB = [
    ("crucial", "adjective", "decisive or critical, especially in the success or failure of something", "Clear communication is crucial during team projects."),
    ("feasible", "adjective", "possible to do easily or conveniently", "Building a bike lane along this route is both safe and feasible."),
    ("substantial", "adjective", "of considerable importance, size, or worth", "The grant provided substantial funding for community sports."),
    ("comprehensive", "adjective", "complete; including all or nearly all elements or aspects", "The guide offers a comprehensive review of all CELPIP tasks."),
    ("advantageous", "adjective", "involving or creating favorable circumstances that increase chances of success", "Carpooling is advantageous for reducing fuel expenses."),
    ("perspective", "noun", "a particular attitude toward or way of regarding something; a point of view", "Listening to diverse perspectives helps teams make better decisions."),
    ("initiative", "noun", "an act or strategy intended to resolve a difficulty or improve a situation", "The city launched a recycling initiative to cut landfill waste."),
    ("implement", "verb", "to put a decision, plan, or agreement into effect", "The company will implement new flexible working hours next month."),
    ("collaborate", "verb", "to work jointly on an activity, especially to produce or create something", "Researchers collaborated with universities across the country."),
    ("significantly", "adverb", "in a sufficiently great or important way as to be worthy of attention", "Regular exercise significantly lowers cardiovascular disease risk."),
    ("prioritize", "verb", "to designate or treat something as more important than other things", "Students should prioritize completing difficult assignments first."),
    ("objective", "noun", "a thing aimed at or sought; a goal", "Our primary objective is to improve customer satisfaction ratings."),
    ("consequence", "noun", "a result or effect of an action or condition", "One consequence of missing the deadline is paying a late fee."),
    ("adequate", "adjective", "satisfactory or acceptable in quality or quantity", "Ensure you get adequate rest the night before the official test."),
    ("accommodate", "verb", "to fit in with the wishes or needs of someone", "The schedule was adjusted to accommodate working parents."),
    ("facilitate", "verb", "to make an action or process easy or easier", "The instructor used visual slides to facilitate group discussion."),
    ("evaluate", "verb", "to form an idea of the amount, number, or value of; assess", "Judges will evaluate presentations based on clarity and evidence."),
    ("sustain", "verb", "to strengthen or support physically or mentally over time", "A healthy diet helps sustain energy levels throughout the workday."),
    ("substitute", "noun", "a person or thing acting or serving in place of another", "Soy milk is a common dairy substitute in many recipes."),
    ("reliable", "adjective", "consistently good in quality or performance; able to be trusted", "Public transit in Vancouver is generally punctual and reliable."),
    ("anticipate", "verb", "to regard as probable; expect or predict", "Commuters should anticipate delays during morning rush hour."),
    ("mandatory", "adjective", "required by law or rules; compulsory", "Wearing a helmet while bicycling on city roads is mandatory."),
    ("eliminate", "verb", "to completely remove or get rid of something", "Automating paperwork helped eliminate common clerical errors."),
    ("reinforce", "verb", "to strengthen or support with additional material or evidence", "The teacher used practice tests to reinforce grammar concepts."),
    ("diverse", "adjective", "showing a great deal of variety; very different", "Toronto is known worldwide for its vibrant, diverse neighborhoods."),
    ("approximate", "adjective", "close to the actual, but not completely accurate or exact", "The approximate driving time from Calgary to Banff is ninety minutes."),
    ("allocate", "verb", "to distribute resources or duties for a particular purpose", "City planners allocated twenty percent of the budget to parks."),
    ("accessible", "adjective", "able to be reached or entered easily by people", "All public library branches are fully wheelchair accessible."),
    ("generate", "verb", "to cause something to arise or come about; produce", "The tourism festival generated millions in revenue for local shops."),
    ("monitor", "verb", "to observe and check the progress or quality of something over time", "Park rangers monitor wildlife populations every spring."),
    ("compensate", "verb", "to give someone something, typically money, in recognition of loss or suffering", "Volunteers were compensated for their travel expenses."),
    ("contribute", "verb", "to give something in order to help achieve or provide something", "Every team member contributed valuable ideas to the project."),
    ("efficient", "adjective", "achieving maximum productivity with minimum wasted effort or expense", "Heat pumps are among the most efficient heating systems available."),
    ("fundamental", "adjective", "forming a necessary base or core; of central importance", "Grammar accuracy and vocabulary range are fundamental for CLB 10."),
    ("indicate", "verb", "to point out or show evidence of something", "Survey results indicate that most residents favor a new dog park."),
    ("inevitable", "adjective", "certain to happen; unavoidable", "Some initial challenges are inevitable when moving to a new country."),
    ("innovative", "adjective", "featuring new methods; advanced and original", "The startup introduced an innovative way to compost kitchen scraps."),
    ("integrate", "verb", "to combine one thing with another so that they become a whole", "The school program helps newcomer youth integrate into the community."),
    ("justify", "verb", "to show or prove to be right or reasonable", "You must justify your choice in the survey response task."),
    ("minimize", "verb", "to reduce something, especially something undesirable, to the smallest possible amount", "Carsharing helps minimize urban parking congestion."),
    ("potential", "noun", "latent qualities or abilities that may be developed and lead to future success", "The employee demonstrated great potential for leadership roles."),
    ("prohibit", "verb", "to formally forbid something by law, rule, or other authority", "Provincial park regulations prohibit open fires during dry spells."),
    ("regulate", "verb", "to control or maintain the rate or speed of a machine or process", "Municipal bylaws regulate noise levels in residential neighborhoods."),
    ("restrict", "verb", "to put a limit on; keep under control", "Parking is restricted to residents with permits on this street."),
    ("retain", "verb", "to continue to have something; keep possession of", "Retain your receipts in case you need to return an item."),
    ("specify", "verb", "to identify clearly and definitely", "The job posting specifies a requirement for five years of experience."),
    ("sufficient", "adjective", "enough; adequate for the purpose", "A two-hour layover is sufficient time to clear customs in Toronto."),
    ("temporary", "adjective", "lasting for only a limited period of time; not permanent", "Roadwork caused a temporary closure of the northbound lane."),
    ("ultimately", "adverb", "finally, in the end, after a series of events", "Hard work and consistent practice ultimately led to her CLB 9."),
    ("utilize", "verb", "to make practical and effective use of", "Test takers should utilize their preparation time strategically.")
]

def populate_words_in_file(path: str):
    filename = os.path.basename(path)
    bundle_slug = filename.replace("words_", "").replace(".html", "")
    
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find all dummy word objects in RSC: {\"id\":\"locked-X\",\"word\":\"DUMMY\"...}
    dummy_pattern = r'\{\\"id\\":\\"(?:locked-\d+|cml[a-z0-9]+)\\",\\"word\\":\\"([a-z]+)\\",\\"definition\\":(?:null|\\"[^\\"]*\\"),\\"example\\":(?:null|\\"[^\\"]*\\"),\\"partOfSpeech\\":\\"([^\\"]*)\\",\\"pronunciation\\":(?:null|\\"[^\\"]*\\"),\\"synonyms\\":(?:null|\\"[^\\"]*\\"),\\"tip\\":(?:null|\\"[^\\"]*\\"),\\"order\\":(\d+),\\"locked\\":(?:true|false)'
    
    matches = list(re.finditer(dummy_pattern, content))
    if not matches:
        return False
        
    bank = VOCAB_BANKS.get(bundle_slug, GENERIC_CELPIP_VOCAB)
    
    replacements = 0
    new_content = content
    
    for i, m in enumerate(matches):
        old_word = m.group(1)
        # Check if old_word looks like random scrambled letters (length >= 4 and no vowels or all lowercase gibberish)
        # If it\x27s a dummy word like "izkdaqsdkvuvtj", replace it with bank[i % len(bank)]
        is_dummy = m.group(0).startswith('{\\"id\\":\\"locked-') or (len(old_word) > 4 and not any(v in old_word for v in ['a','e','i','o','u']))
        if 'locked' in m.group(0) or is_dummy:
            replacement_item = bank[i % len(bank)]
            rep_word, rep_pos, rep_def, rep_ex = replacement_item
            
            # Construct new JSON object
            new_obj = (
                f'{{\\"id\\":\\"word-{bundle_slug}-{i+1}\\",'
                f'\\"word\\":\\"{rep_word}\\",'
                f'\\"definition\\":\\"{rep_def}\\",'
                f'\\"example\\":\\"{rep_ex}\\",'
                f'\\"partOfSpeech\\":\\"{rep_pos}\\",'
                f'\\"pronunciation\\":null,'
                f'\\"synonyms\\":null,'
                f'\\"tip\\":null,'
                f'\\"order\\":{m.group(3)},'
                f'\\"locked\\":false'
            )
            
            # Replace RSC match
            new_content = new_content.replace(m.group(0), new_obj)
            
            # Also replace in DOM: the scrambled word text in the button
            # <span ...>{old_word}</span><span ...>This word unlocks... or definition
            dom_old_word = f'>{old_word}</span>'
            dom_new_word = f'>{rep_word}</span>'
            if dom_old_word in new_content:
                new_content = new_content.replace(dom_old_word, dom_new_word, 1)
            
            replacements += 1
            
    if new_content != content:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Populated {replacements} authentic vocabulary words in {filename}")
        return True
    return False

def main():
    files = sorted(glob.glob(os.path.join(PAGES_DIR, "words_*.html")))
    total_populated = 0
    for p in files:
        if populate_words_in_file(p):
            total_populated += 1
    print(f"Finished populating authentic vocabulary across {total_populated} bundle pages.")

if __name__ == "__main__":
    main()
