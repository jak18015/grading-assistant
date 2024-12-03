import time
from assets import GradingAssistant, rubric

def main():
    time_start = time.time()

    rubric_data = rubric("assets/rubric.json")
    assistant = GradingAssistant(rubric_data)
    assistant.iterate_over_dictionary(assistant.rubric_dict)
    assistant.summarize()
    
    time_end = time.time()

    duration = round((time_end - time_start)/60, 1)
    print(f'\n{duration} minutes')
    
if __name__ == "__main__":
    main()
