# Developing crew with meshing up agents and tasks

# from crewai import Crew,Process
# from agents import researcher,writer
# from tasks import researchtask,writertask

# crew = Crew(
#     agents=[researcher,writer],
#     tasks=[researchtask,writertask],
#     process=Process.sequential, # After the research agent finishes it's work it will collaborate to news writer
# )

# Kicking off the crew

# outcome = crew.kickoff(inputs={'topic':'Develop a company list to shortlist for contract manufacturing of sauces, condiments and - Bouillon - ⁠Stock Cubes and Powders). The companies should be located near Bangalore and Hosur, and they should have food scientists or technologists who can recreate the taste of a specific sauce. Where to look for: Industry boards and associations: There are a number of industry boards and associations that can provide you with information about contract manufacturers. These organizations can also connect you with potential suppliers. Trade shows: Attending trade shows is a great way to meet potential contract manufacturers. You can also learn about the latest industry trends and technologies at trade shows. Referrals: Ask your friends, colleagues, and business partners for referrals to contract manufacturers.'})
# print(outcome)

# Non 2024 - Contract Manufacturers in Sauces and Condiments

# from crewai import Crew, Process
# from agents import researcher, writer
# from tasks import researchtask, writertask

# # Create a crew focused on finding contract manufacturers for sauces
# crew = Crew(
#     agents=[researcher, writer],
#     tasks=[researchtask, writertask],
#     process=Process.sequential  # Research findings inform the strategic report
# )

# # Launch research and reporting on contract manufacturers
# outcome = crew.kickoff(inputs={
#     'topic': 'Identifying Contract Manufacturers for Sauces and Condiments near Bangalore and Hosur'
# })
# print(outcome)

# 2024 - Contract Manufacturers in Sauces and Condiments

from crewai import Crew, Process
from agents import researcher, verifier, writer
from tasks import researchtask, verificationtask, writertask

# Create a specialized crew for 2024 contract manufacturing research
crew = Crew(
    agents=[researcher, verifier, writer],
    tasks=[researchtask, verificationtask, writertask],
    process=Process.sequential  # Ensure sequential processing of tasks
)

# Launch 2024 research on contract manufacturers
outcome = crew.kickoff(inputs={
    'topic': 'Identifying 2024 Contract Manufacturers for Sauces, Condiments, Bouillon, Stock Cubes, and Powders near Bangalore and Hosur',
    'year': 2024,
    'region': 'Bangalore and Hosur',
    'focus_areas': [
        'Sauces', 
        'Condiments', 
        'Bouillon', 
        'Stock Cubes', 
        'Powders'
    ]
})
print(outcome)