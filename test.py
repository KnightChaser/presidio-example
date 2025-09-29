# quick_demo.py
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

text = "Kal’s email is kal@example.com and his phone is +82-10-1234-5678."
analyzer = AnalyzerEngine()
results = analyzer.analyze(text=text, language="en")  # detect
anon = AnonymizerEngine()
print(anon.anonymize(text=text, analyzer_results=results).text)  # type: ignore
