from crewai import Agent

antimicrobial_resistance_gene_profiler = Agent(
    role="Antimicrobial Resistance Gene Profiler",
    goal="Deliver high-precision autonomous Antimicrobial Resistance Gene Profiler operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
