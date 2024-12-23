# Defining tasks for all the agents

# from crewai import Task # For defining task
# from tools import tool
# from agents import researcher,writer

# researchtask = Task(
#     description = (
#         "Identify the next big trend in {topic}."
#         "Focus on identifying pros and cons and the overall narrative."
#         "Your final report should clearly articulate the key points,"
#         "its market opportunities, and potential risks."),
#     expected_output = 'A collection of recent news articles, with a summary of each article highlighting the main points and publication dates.',
#     tools = [tool],
#     agent = researcher # Defining agent
# )

# writertask = Task(
#     description = (
#         "Compose an insightful article on {topic}."
#         "Focus on the latest trends and how it's impacting the industry."
#         "This article should be easy to understand, engaging, and positive."),
#     expected_output = 'A polished final draft of the article, free of grammatical errors and inconsistencies, ready for publication.',
#     tools = [tool],
#     agent = writer, # Defining agent
#     async_execution = False,
#     output_file = 'launchpad.md' # Output file as markdown
    
# )

# Non 2024 - Contract Manufacturers in Sauces and Condiments

# from crewai import Task
# from tools import tool
# from agents import researcher, writer

# # Research task to identify contract manufacturers
# researchtask = Task(
#     description=(
#         "Conduct comprehensive research on contract manufacturers specializing in sauces and condiments. "
#         "Focus on companies near Bangalore and Hosur with advanced food science capabilities. "
#         "Investigate industry boards, trade associations, and potential referral networks. "
#         "Evaluate each manufacturer's technical capabilities, specifically their ability to recreate specific sauce tastes."
#     ),
#     expected_output=(
#         "A detailed spreadsheet listing potential contract manufacturers, including: "
#         "Company name, location, specialization, food science team credentials, "
#         "contact information, and preliminary assessment of sauce recreation capabilities."
#     ),
#     tools=[tool],
#     agent=researcher
# )

# # Writing task to compile research into a strategic report
# writertask = Task(
#     description=(
#         "Develop a strategic report summarizing findings on contract manufacturers. "
#         "Highlight key manufacturers, their unique capabilities, potential collaboration opportunities, "
#         "and recommendations for further engagement. Ensure the report is professional, "
#         "data-driven, and provides clear strategic insights."
#     ),
#     expected_output=(
#         "A comprehensive PDF report with executive summary, detailed manufacturer profiles, "
#         "comparative analysis, and strategic recommendations for sauce contract manufacturing."
#     ),
#     tools=[tool],
#     agent=writer,
#     async_execution=False,
#     output_file='contract_manufacturers_report_llama3_70b.md'
# )

# Contract Manufacturers in Sauces and Condiments

from crewai import Task
from tools import tool
from agents import researcher, verifier, writer

# Comprehensive research task for 2024 contract manufacturers
researchtask = Task(
    description=(
        "Conduct an in-depth investigation of contract manufacturers in sauces, condiments, "
        "bouillon, stock cubes, and powders near Bangalore and Hosur. "
        "Specifically focus on:"
        "1. Companies with advanced food science capabilities"
        "2. Recent technological advancements in sauce production"
        "3. Emerging trends in contract manufacturing"
        "4. Specific capabilities in taste recreation"
        "5. Verify information from multiple sources including:"
        "   - Industry boards and associations"
        "   - trade show records"
        "   - Government diretories of Tamilnadu, karnataka and MSME"
        "   - Website link"
        "   - Recent referral networks"
        "   - Digital and professional platforms"
    ),
    expected_output=(
        "Comprehensive 2024 database including:"
        "- Company names and contact details"
        "- Specific food science capabilities"
        "- Government diretories of Tamilnadu, karnataka and MSME"
        "- Website link"
        "- Technological specializations"
        "- Verified contact information"
        "- Assessment of taste recreation capabilities"
    ),
    tools=[tool],
    agent=researcher
)

# Verification task to ensure research accuracy
verificationtask = Task(
    description=(
        "Meticulously verify and cross-reference all research findings. "
        "Validate the accuracy of company information, technological capabilities, "
        "and market positioning as of 2024. "
        "Identify any discrepancies or additional insights missed in initial research."
    ),
    expected_output=(
        "Verification report highlighting:"
        "- Confirmed information"
        "- Potential discrepancies"
        "- Additional insights"
        "- Recommendation for further investigation"
    ),
    tools=[tool],
    agent=verifier
)

# Updated writing task to compile verified research
writertask = Task(
    description=(
        "Compile a detailed and comprehensive database report on contract manufacturers for sauces, condiments, "
        "bouillon, stock cubes, and powders in Bangalore and Hosur. "
        "Integrate verified research findings to highlight manufacturer capabilities, technological advancements, "
        "and emerging trends. Assess taste recreation capabilities and include strategic insights for decision-making."
    ),
    expected_output=(
        "Definitive report including:"
        "- Executive summary of findings"
        "- Detailed profiles of 30 verified manufacturers"
        "- Contact details and website links"
        "- Specific food science capabilities and technological specializations"
        "- Assessment of taste recreation capabilities"
        "- Insights into emerging trends and advancements in contract manufacturing"
        "- Verified contact information from multiple sources"
        "- Strategic recommendations for partnerships"
        "- Future outlook for contract manufacturing in this sector"
    ),
    tools=[tool],
    agent=writer,
    async_execution=False,
    output_file='2024_verified_contract_manufacturers_report.md'
)
