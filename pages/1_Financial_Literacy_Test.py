import streamlit as st

st.set_page_config(page_title="Financial Literacy Assessment", page_icon="🧠", layout="wide")

st.title("🧠 Financial Literacy Assessment")
st.markdown("Welcome! Take this quick check-in to see how comfortably you navigate today's financial system and discover accessible ways to grow your money.")

# --- QUESTION BANK (5 Questions per Batch per Level) ---
QUESTION_BANK = {
    1: {  # LEVEL 1: ACCOUNTS & SYSTEM BASICS
        "title": "Level 1: Everyday Accounts & Managing Cash",
        "batches": [
            # Batch 0
            [
                {
                    "question": "1. What is a brokerage account?",
                    "options": [
                        "A special loan account used only for buying physical real estate",
                        "An account that lets you buy, sell, and hold investments like stocks, ETFs, and cash funds",
                        "A state-run tax account that collects sales tax",
                        "A bank account that charges fees every time you deposit cash"
                    ],
                    "answer": 1,
                    "explanation": "A brokerage account is simply your doorway to the investment world. Unlike a standard checking account, it lets you easily buy shares of companies, index funds, or cash-yielding funds."
                },
                {
                    "question": "2. What is the main difference between a checking account and a savings account?",
                    "options": [
                        "Checking accounts are for daily transactions; savings accounts are designed to hold money and earn interest",
                        "Savings accounts give you a debit card for groceries; checking accounts do not",
                        "Checking accounts automatically invest your money in the stock market",
                        "There is no difference between them"
                    ],
                    "answer": 0,
                    "explanation": "Checking accounts are your 'traffic hub' for paying monthly bills. Savings accounts (especially High-Yield Savings Accounts) are meant to keep your reserves growing safely until you need them."
                },
                {
                    "question": "3. What is an Emergency Fund?",
                    "options": [
                        "A high-risk account used for day trading stocks",
                        "Cash set aside in a safe, accessible account to cover 3–6 months of living expenses if unexpected costs arise",
                        "A line of credit from a credit card company",
                        "A tax payment paid to the IRS at the end of the year"
                    ],
                    "answer": 1,
                    "explanation": "An emergency fund acts as your personal financial safety net. It protects you from having to borrow money or take on high-interest debt when unexpected events happen."
                },
                {
                    "question": "4. What does the term 'Inflation' mean in everyday terms?",
                    "options": [
                        "When your bank increases the interest rate on your savings account",
                        "The gradual rise in prices over time, which means a dollar buys a little less than it used to",
                        "A sudden drop in stock market prices",
                        "The total tax rate on your annual income"
                    ],
                    "answer": 1,
                    "explanation": "Inflation is simply the rising cost of living over time. Keeping all your long-term cash in a traditional checking account causes your purchasing power to slowly shrink against inflation."
                },
                {
                    "question": "5. What is the habit of 'Paying Yourself First'?",
                    "options": [
                        "Paying all your bills and spending on lifestyle first, then saving whatever cash happens to be left over",
                        "Automatically transferring a portion of your income straight into savings or investments on payday",
                        "Using credit card reward points to buy personal items",
                        "Paying off your lowest-interest loan before buying groceries"
                    ],
                    "answer": 1,
                    "explanation": "'Pay yourself first' means treating your future savings like an essential bill. Automating it on payday ensures your long-term goals get funded without relying on leftover cash."
                }
            ],
            # Batch 1
            [
                {
                    "question": "1. What is a High-Yield Savings Account (HYSA)?",
                    "options": [
                        "A risky stock investment account with no insurance",
                        "A bank savings account that pays significantly higher interest than traditional checking/savings accounts while keeping your cash safe",
                        "A retirement account you cannot touch until age 65",
                        "A loan account used to buy a car"
                    ],
                    "answer": 1,
                    "explanation": "HYSAs work just like standard bank savings accounts, but they pass actual market interest rates back to you—helping your cash fight off inflation with virtually zero added risk."
                },
                {
                    "question": "2. What is a credit score used for?",
                    "options": [
                        "It measures how much total money you have saved in your bank account",
                        "It measures how reliably you repay borrowed money, helping lenders determine interest rates for loans or mortgages",
                        "It determines your federal income tax bracket",
                        "It dictates how many stock shares you are allowed to buy"
                    ],
                    "answer": 1,
                    "explanation": "Your credit score is a track record of borrowing reliability. A higher score helps you qualify for lower interest rates when financing major purchases like a house or car."
                },
                {
                    "question": "3. Why is high-interest credit card debt considered a major obstacle to building wealth?",
                    "options": [
                        "Because high interest rates (often 20%+) compound against you, costing far more money than standard investments can earn",
                        "Because credit cards aren't accepted at most retail stores",
                        "Because credit card companies report your purchases to your employer",
                        "Because you are legally required to pay off your balance in 24 hours"
                    ],
                    "answer": 0,
                    "explanation": "Carrying high-interest debt acts like a reverse investment. Eliminating a 20% interest card balance is equivalent to earning a guaranteed 20% return on your money!"
                },
                {
                    "question": "4. What is a Certificate of Deposit (CD)?",
                    "options": [
                        "A type of physical stock certificate issued by digital companies",
                        "An agreement with a bank where you lock up cash for a fixed term (like 12 months) in exchange for a guaranteed interest rate",
                        "A government tax form for reporting income",
                        "A digital wallet for storing online cash"
                    ],
                    "answer": 1,
                    "explanation": "CDs are simple savings products. In exchange for agreeing to leave your money untouched for a set period, the bank guarantees you a specific, fixed interest rate."
                },
                {
                    "question": "5. What is the main benefit of setting up automatic bill pay or automatic transfers?",
                    "options": [
                        "It removes human memory and temptation, ensuring your bills are paid on time and savings grow effortlessly",
                        "It eliminates income taxes on your paycheck",
                        "It guarantees you will double your investment money each year",
                        "It forces your bank to waive all transaction fees"
                    ],
                    "answer": 0,
                    "explanation": "Automation creates consistent habits without requiring constant discipline or memory, helping you avoid late fees and build savings seamlessly."
                }
            ]
        ]
    },
    2: {  # LEVEL 2: BUILDING BLOCKS OF INVESTING
        "title": "Level 2: Building Blocks of Investing",
        "batches": [
            # Batch 0
            [
                {
                    "question": "1. What are the main types of investments available to regular investors?",
                    "options": [
                        "Only physical cash currency and real estate property",
                        "Stocks (owning pieces of companies), Bonds (loaning money for interest), ETFs/Funds, and Cash/Yield accounts",
                        "Only lottery tickets and precious metals",
                        "Government tax receipts and foreign currency physical bills"
                    ],
                    "answer": 1,
                    "explanation": "Modern investing offers straightforward building blocks: Stocks for long-term growth, Bonds/Cash for income and stability, and ETFs to bundle them together easily."
                },
                {
                    "question": "2. What is an Exchange-Traded Fund (ETF)?",
                    "options": [
                        "A single private company stock that only trades once per year",
                        "A convenient 'basket' of many different stocks or bonds that you can buy in a single trade",
                        "A government tax program for small business owners",
                        "A digital currency used only for online video games"
                    ],
                    "answer": 1,
                    "explanation": "An ETF acts like a pre-packaged bundle. Instead of picking 500 individual companies, buying one S&P 500 ETF gives you instant fractional ownership in all 500 at once."
                },
                {
                    "question": "3. What is Bitcoin?",
                    "options": [
                        "A physical gold coin stored in central bank vaults",
                        "A decentralized digital currency built on a global network that allows peer-to-peer transfers without relying on a central bank",
                        "A new type of corporate bond issued by technology firms",
                        "An official paper currency issued by the U.S. Treasury"
                    ],
                    "answer": 1,
                    "explanation": "Bitcoin is a digital asset that operates on a public network (blockchain). Unlike traditional fiat currency, its total supply limit and transactions are managed by software rules rather than a government."
                },
                {
                    "question": "4. What is a stock dividend?",
                    "options": [
                        "A fee you must pay to the stock market every month",
                        "A cash payout that profitable companies share directly with their stockholders, usually every quarter",
                        "The interest rate charged by a bank on a mortgage loan",
                        "The original cost of launching a new company"
                    ],
                    "answer": 1,
                    "explanation": "When companies make a profit, many choose to pay out a portion of that cash directly to their owners (shareholders) as quarterly dividend income."
                },
                {
                    "question": "5. What does 'Diversification' mean in plain language?",
                    "options": [
                        "Putting all your investment money into your single favorite company",
                        "Not putting all your eggs in one basket—spreading money across different assets so one bad piece of news doesn't ruin your portfolio",
                        "Selling all your assets whenever the stock market goes down",
                        "Keeping 100% of your savings stored in cash under your mattress"
                    ],
                    "answer": 1,
                    "explanation": "Diversification protects your wealth. If one company runs into trouble, having your money spread across dozens or hundreds of assets keeps your overall portfolio safe."
                }
            ],
            # Batch 1
            [
                {
                    "question": "1. What is an Index Fund?",
                    "options": [
                        "A specialized fund designed to track an entire market index (like the top 500 companies in the US) automatically and at very low cost",
                        "A high-fee account where a fund manager trades stocks daily",
                        "A bank loan used to buy foreign real estate",
                        "An insurance contract that guarantees zero market drops"
                    ],
                    "answer": 0,
                    "explanation": "Index funds track broad market performance automatically. They offer an easy, low-cost way for anyone to own a piece of the overall economy."
                },
                {
                    "question": "2. What is the main difference between a Stock and a Bond?",
                    "options": [
                        "Stocks represent piece-ownership in a business; Bonds are loans you make to a government or business in exchange for regular interest payments",
                        "Bonds give you voting power in a company; Stocks do not",
                        "Stocks are issued by banks; Bonds are issued by small local businesses",
                        "There is no difference between them"
                    ],
                    "answer": 0,
                    "explanation": "With stocks, you are an owner participating in company growth. With bonds, you are a lender earning fixed interest income."
                },
                {
                    "question": "3. What is Dollar-Cost Averaging (DCA)?",
                    "options": [
                        "Trying to guess the exact low point of the market before putting any money in",
                        "Investing a set amount of money at regular intervals (like $100 every payday), regardless of whether prices are up or down",
                        "Exchanging US dollars for foreign currencies at local airports",
                        "Selling all your investments at the end of every calendar year"
                    ],
                    "answer": 1,
                    "explanation": "Dollar-cost averaging removes the guesswork and stress of market timing. You automatically buy more shares when prices are low and fewer when prices are high."
                },
                {
                    "question": "4. What is the Rule of 72 useful for?",
                    "options": [
                        "Calculating your exact monthly tax bill",
                        "Estimating roughly how many years it will take your investment to double by dividing 72 by your annual interest rate",
                        "Determining how much credit card debt you can safely carry",
                        "Finding out the maximum number of stocks you should own"
                    ],
                    "answer": 1,
                    "explanation": "The Rule of 72 is a quick mental math tool! For instance, at a 7% annual return, 72 ÷ 7 means your money doubles roughly every 10 years."
                },
                {
                    "question": "5. What is Compound Interest?",
                    "options": [
                        "Interest calculated only on your original initial deposit",
                        "Growth that happens when you earn interest on both your original deposit AND on the interest you've already accumulated",
                        "A penalty fee charged for transferring money between bank accounts",
                        "A fixed state tax applied to savings accounts"
                    ],
                    "answer": 1,
                    "explanation": "Compound interest creates a snowball effect! As your accumulated earnings start generating their own earnings, your money grows exponentially over time."
                }
            ]
        ]
    },
    3: {  # LEVEL 3: RETIREMENT & GROWING WEALTH TAX-EFFICIENTLY
        "title": "Level 3: Tax-Smart Accounts & Wealth Strategies",
        "batches": [
            # Batch 0
            [
                {
                    "question": "1. What is a Roth IRA and why do so many people use it?",
                    "options": [
                        "A company-sponsored loan program for buying corporate shares",
                        "An individual retirement account where your money grows 100% tax-free, and qualified withdrawals in retirement are completely tax-free",
                        "A high-fee bank account with strict monthly maintenance charges",
                        "A taxable account that requires paying capital gains tax every quarter"
                    ],
                    "answer": 1,
                    "explanation": "With a Roth IRA, you put in money that has already been taxed. In return, all future growth and distributions in retirement are completely tax-free!"
                },
                {
                    "question": "2. What is a 401(k) or 403(b) plan?",
                    "options": [
                        "A retirement savings plan offered by employers, often allowing you to invest money directly out of your paycheck",
                        "A loan program for purchasing rental properties",
                        "A state-issued debit card for healthcare expenses",
                        "A short-term savings account managed by credit bureaus"
                    ],
                    "answer": 0,
                    "explanation": "Employer plans like 401(k)s make investing automatic by deducting money straight from your paycheck before or after taxes into your investment account."
                },
                {
                    "question": "3. What does an 'Employer Match' mean in a 401(k)?",
                    "options": [
                        "Your employer matches your job performance score to your pay rate",
                        "Free money! Your employer contributes extra dollars to your retirement account to match what you put in up to a set percentage",
                        "Your employer requires you to buy shares of company stock",
                        "Your employer pays your monthly credit card bill"
                    ],
                    "answer": 1,
                    "explanation": "An employer match is essentially free money on top of your salary. Getting the full match should almost always be a top priority!"
                },
                {
                    "question": "4. What is a Money Market Fund (like SPAXX)?",
                    "options": [
                        "A high-risk technology stock fund",
                        "A very safe, liquid mutual fund that invests in high-quality short-term debt to pay competitive cash yields",
                        "A physical currency exchange booth",
                        "A non-profit charitable trust fund"
                    ],
                    "answer": 1,
                    "explanation": "Money market funds offer a low-risk, highly liquid place to park cash while earning higher interest rates than traditional checking accounts."
                },
                {
                    "question": "5. Why is starting to invest early so impactful, even with small monthly amounts?",
                    "options": [
                        "Because early investors are exempt from paying taxes",
                        "Because more time allows compound growth to work its magic—giving your returns decades to snowball",
                        "Because stock prices are always lower for younger investors",
                        "Because banks pay higher interest rates to new accounts"
                    ],
                    "answer": 1,
                    "explanation": "Time is the single greatest superpower in investing! Starting early gives compound interest decades to build your money, even if you start small."
                }
            ],
            # Batch 1
            [
                {
                    "question": "1. What is the difference between a Traditional IRA and a Roth IRA?",
                    "options": [
                        "Traditional IRAs give you a tax deduction today but you pay tax later in retirement; Roth IRAs use after-tax money today so you enjoy tax-free withdrawals later",
                        "Traditional IRAs can only hold cash; Roth IRAs can only hold real estate",
                        "Roth IRAs are only offered by state governments; Traditional IRAs are offered by employers",
                        "There is no difference between them"
                    ],
                    "answer": 0,
                    "explanation": "It comes down to *when* you pay taxes: Traditional gives you a break today, while Roth gives you tax-free growth and withdrawals down the road."
                },
                {
                    "question": "2. What is Capital Gain?",
                    "options": [
                        "The monthly fee charged by your bank for maintaining a checking account",
                        "The profit you make when you sell an investment for a higher price than what you originally paid for it",
                        "The interest rate paid on government savings bonds",
                        "The total debt owed on a credit card balance"
                    ],
                    "answer": 1,
                    "explanation": "If you buy an ETF share for $100 and sell it years later for $250, that $150 increase is your capital gain."
                },
                {
                    "question": "3. What is a Health Savings Account (HSA)?",
                    "options": [
                        "A health insurance plan that only covers emergency rooms",
                        "A tax-advantaged account used for qualified medical expenses that offers a 'triple tax benefit'",
                        "A specialized loan account for medical school tuition",
                        "A discount program for gym memberships"
                    ],
                    "answer": 1,
                    "explanation": "HSAs are incredibly tax-smart! Contributions lower your taxable income, the money grows tax-free, and withdrawals for medical costs are 100% tax-free."
                },
                {
                    "question": "4. What is an expense ratio on an ETF or Index Fund?",
                    "options": [
                        "The annual fee percentage deducted by the fund manager to cover operational costs",
                        "The tax rate charged by state governments on dividend checks",
                        "The percentage of cash you must keep in your checking account",
                        "The penalty charged for withdrawing money before age 59½"
                    ],
                    "answer": 0,
                    "explanation": "An expense ratio is the tiny fee taken automatically to run the fund. Broad index funds usually have ultra-low expense ratios (like 0.03% to 0.10%)."
                },
                {
                    "question": "5. What is the core goal of aligning your cash flow with an investment plan?",
                    "options": [
                        "To try to beat professional Wall Street traders every single day",
                        "To make growing your wealth regular, predictable, and aligned with your personal life goals without taking unnecessary risk",
                        "To avoid using banks or credit unions altogether",
                        "To maximize the amount of taxes you pay each year"
                    ],
                    "answer": 1,
                    "explanation": "Investing isn't about gambling or stress. It's simply about setting up clear system pathways so your hard-earned cash works to support your future."
                }
            ]
        ]
    },
    4: {  # LEVEL 4: MODERN WEALTH TOOLS & CASH OPTIONS
        "title": "Level 4: Modern Cash Tools, Yields & Security",
        "batches": [
            # Batch 0
            [
                {
                    "question": "1. What is an Ultra-Short Duration Bond ETF (like PULS)?",
                    "options": [
                        "A high-risk fund that buys speculative tech stocks",
                        "An ETF holding very short-term debt that offers attractive yields with minimal price volatility",
                        "A long-term real estate fund that requires 5-year lockups",
                        "A digital wallet used strictly for cryptocurrency"
                    ],
                    "answer": 1,
                    "explanation": "Ultra-short bond ETFs hold bonds maturing in very short timeframes. They provide higher yields than traditional checking while shielding your principal from big rate fluctuations."
                },
                {
                    "question": "2. What is FDIC or SIPC Insurance designed to do?",
                    "options": [
                        "Protect your bank cash (FDIC) or brokerage securities (SIPC) if the financial institution goes bankrupt",
                        "Guarantee that your stock investments will never drop in value",
                        "Pay off your credit card balance if you lose your job",
                        "Protect your home from property value decreases"
                    ],
                    "answer": 0,
                    "explanation": "FDIC (for banks) and SIPC (for brokerages) act as systemic safety nets. They protect your deposits and assets if the underlying financial institution fails."
                },
                {
                    "question": "3. What is a U.S. Treasury Bill (T-Bill)?",
                    "options": [
                        "A paper coupon used to pay federal taxes at a discount",
                        "A short-term loan you make directly to the U.S. government that pays interest and is backed by government credit",
                        "A loan extended to corporate startups",
                        "A type of stock traded on overseas exchanges"
                    ],
                    "answer": 1,
                    "explanation": "T-Bills are ultra-safe, short-term debt instruments issued by the U.S. government. They are virtually risk-free from default and exempt from state/local income taxes!"
                },
                {
                    "question": "4. What is Two-Factor Authentication (2FA) and why should you use it on financial accounts?",
                    "options": [
                        "A tax-filing step that doubles your annual refund",
                        "A security setting requiring two forms of verification (like a password and a phone code) to prevent unauthorized access",
                        "A bank rule that requires two signatures to open an account",
                        "An investment strategy using two separate brokerage firms"
                    ],
                    "answer": 1,
                    "explanation": "2FA adds a vital second layer of defense. Even if someone steals your account password, they cannot log in without your second verification step."
                },
                {
                    "question": "5. What is the difference between a Fixed-Income asset and an Equity asset?",
                    "options": [
                        "Fixed-Income pays predictable interest/yield (like bonds or Treasury bills); Equity represents ownership growth (like company stocks)",
                        "Fixed-Income carries higher risk than Equity",
                        "Equity is issued by central banks; Fixed-Income is issued by retail stores",
                        "There is no difference between them"
                    ],
                    "answer": 0,
                    "explanation": "Fixed-income assets provide regular income payments with lower volatility, while equity assets focus on capital growth over time."
                }
            ],
            # Batch 1
            [
                {
                    "question": "1. What is a Yield Curve?",
                    "options": [
                        "A line graph showing the relationship between interest rates and different bond maturity lengths",
                        "A chart showing stock market price dips during a recession",
                        "The tax rate curve applied to corporate dividends",
                        "A spending graph inside a monthly budgeting app"
                    ],
                    "answer": 0,
                    "explanation": "The yield curve shows what interest rates bonds pay across different timeframes (e.g., 3 months vs. 10 years), giving clues about economic conditions."
                },
                {
                    "question": "2. Why are Treasury Bills (T-Bills) often tax-advantaged compared to bank interest?",
                    "options": [
                        "They are completely free from federal income tax",
                        "Their interest income is exempt from state and local income taxes",
                        "They eliminate capital gains taxes on stock trades",
                        "They can be bought using pre-tax paycheck dollars"
                    ],
                    "answer": 1,
                    "explanation": "Interest earned from U.S. Treasuries is exempt from state and local income taxes—making them especially attractive for investors living in states with income taxes!"
                },
                {
                    "question": "3. What is a Target-Date Fund?",
                    "options": [
                        "A fund that automatically shifts its asset mix from aggressive growth toward safer income as you get closer to a targeted retirement year",
                        "A high-frequency trading algorithm used by Wall Street banks",
                        "A bank account that locks up cash until a specific birthday",
                        "A real estate fund that buys rental properties on set calendar dates"
                    ],
                    "answer": 0,
                    "explanation": "Target-date funds offer hands-off simplicity. You pick your target retirement year (e.g., 2050), and the fund handles rebalancing to safer assets as that year approaches."
                },
                {
                    "question": "4. What is the main risk of holding excess long-term cash in a standard 0.01% checking account?",
                    "options": [
                        "The bank will lock your account after 30 days",
                        "Your cash steadily loses purchasing power every year to monetary inflation and missed interest yield",
                        "Your bank balance will automatically decrease every month",
                        "You will be fined by credit rating agencies"
                    ],
                    "answer": 1,
                    "explanation": "Holding excess long-term cash in standard checking creates an opportunity cost: you miss out on interest yield while inflation erodes the value of your dollars."
                },
                {
                    "question": "5. What is the overall benefit of setting up an integrated financial system (checking + HYSA/Cash Yield + Roth IRA/Brokerage)?",
                    "options": [
                        "It makes building wealth structural and stress-free—directing money automatically into cash safety, income, and long-term growth",
                        "It guarantees zero taxes on all stock sales",
                        "It allows you to bypass credit checks permanently",
                        "It doubles your employer salary automatically"
                    ],
                    "answer": 0,
                    "explanation": "When your accounts work together automatically, you don't have to stress over daily market moves—your financial system handles cash protection and growth for you!"
                }
            ]
        ]
    }
}

# --- SESSION STATE MANAGEMENT ---
if "current_level" not in st.session_state:
    st.session_state.current_level = 1
if "batch_index" not in st.session_state:
    st.session_state.batch_index = 0
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# Fetch active level data
lvl = st.session_state.current_level
b_idx = st.session_state.batch_index
level_data = QUESTION_BANK[lvl]
available_batches = len(level_data["batches"])

if b_idx >= available_batches:
    st.session_state.batch_index = 0
    b_idx = 0

current_questions = level_data["batches"][b_idx]

# --- UI HEADER ---
st.subheader(f"🎯 {level_data['title']}")
st.caption(f"Level {lvl} of 4 | Batch {b_idx + 1} of {available_batches}")

st.progress((lvl - 1) / 4 + (b_idx + 1) * 0.125)

# --- QUESTION RENDER ENGINE ---
if not st.session_state.submitted:
    st.markdown("---")
    for idx, q in enumerate(current_questions):
        st.markdown(f"**{q['question']}**")
        choice = st.radio(
            label=f"q_{idx}",
            options=q["options"],
            key=f"q_ans_{lvl}_{b_idx}_{idx}",
            index=None,
            label_visibility="collapsed"
        )
        if choice is not None:
            st.session_state.user_answers[idx] = q["options"].index(choice)
        st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Submit 5 Answers", type="primary", use_container_width=True):
        if len(st.session_state.user_answers) < 5:
            st.warning("Please answer all 5 questions before submitting!")
        else:
            st.session_state.submitted = True
            st.rerun()

# --- RESULTS & NAVIGATION ENGINE ---
else:
    st.markdown("---")
    st.subheader("📊 Results & Friendly Takeaways")
    
    correct_count = 0
    for idx, q in enumerate(current_questions):
        user_choice = st.session_state.user_answers.get(idx, None)
        is_correct = user_choice == q["answer"]
        
        if is_correct:
            correct_count += 1
            st.success(f"**Q{idx + 1}: Correct!** 🟢 {q['question']}")
        else:
            correct_str = q["options"][q["answer"]]
            st.error(f"**Q{idx + 1}: Keep Learning** 🔴 {q['question']}\n\n**Key Concept:** {correct_str}")
        
        st.info(f"💡 **Why this matters:** {q['explanation']}")
        st.markdown("<br>", unsafe_allow_html=True)
    
    score_pct = (correct_count / 5) * 100
    st.markdown("---")
    st.metric(label="Batch Score", value=f"{correct_count} / 5", delta=f"{score_pct:.0f}% Mastery")
    
    st.subheader("What would you like to do next?")
    col_nav1, col_nav2 = st.columns(2)
    
    with col_nav1:
        if b_idx + 1 < available_batches:
            if st.button(f"🔄 Try 5 More Questions at Level {lvl}", use_container_width=True):
                st.session_state.batch_index += 1
                st.session_state.user_answers = {}
                st.session_state.submitted = False
                st.rerun()
        else:
            st.button(f"✅ Level {lvl} Batches Complete", disabled=True, use_container_width=True)

    with col_nav2:
        if lvl < 4:
            if st.button(f"🚀 Advance to Level {lvl + 1}", type="primary", use_container_width=True):
                st.session_state.current_level += 1
                st.session_state.batch_index = 0
                st.session_state.user_answers = {}
                st.session_state.submitted = False
                st.rerun()
        else:
            st.success("🎉 You have completed all 4 levels of the Financial Assessment!")
            if st.button("🔁 Restart Assessment from Level 1", use_container_width=True):
                st.session_state.current_level = 1
                st.session_state.batch_index = 0
                st.session_state.user_answers = {}
                st.session_state.submitted = False
                st.rerun()