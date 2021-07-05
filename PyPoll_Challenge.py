#Main Porpuse -> Analyse the results of the elections

#Reading the csv file 
import csv
import os  
# Assign a variable to load a file from a path.
file_to_load = os.path.join(r"C:\Users\Hana\Documents\Data_Analytics_BootCam\Module_3\Election_Analysis","election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join(r"C:\Users\Hana\Documents\Data_Analytics_BootCam\Module_3\Election_Analysis\analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Print the header row.
    headers = next(file_reader)
    #Decere a list for the names of candidates
    candidate_options = []
    county_options = []
    #Declere a dictionary to save the votes for each candidate
    candidate_votes = {}
    county_votes = {}
    #Variabe for winning candidate and county
    winnnig_candidate = {}
    winning_count = 0 
    winning_percentage = 0
    county_turnout = 0
    county_turnout_percentage = 0
    winning_county= {}

    #Count each row from de CSV File
    for row in file_reader:
        total_votes += 1 
    
        # Print the candidate name from each row.
        candidate_name = row[2]
        county_name = row[1]
        
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            #Adding the keys for our dictiorary for the candidates
            candidate_votes[candidate_name] = 0 
        if county_name not in county_options:
            county_options.append(county_name)
             #Adding the keys for our dictiorary for the candidates
            county_votes[county_name] = 0 

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        county_votes[county_name] += 1  

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"\nTotal Votes: {total_votes:,}\n"
        f"\n-------------------------\n"
        f"\nCounty Votes:\n"
        f"\n")
    print(election_results, end="") 
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results) 

     # Determine the percentage of votes for each county by looping through the counts.
    for county_name in county_votes:
        votes_county = county_votes[county_name]
        vote_per_county = float(votes_county) / float(total_votes) * 100
        # To do: print out each county's name, vote count, and percentage of
        county_results = (f"{county_name}:{vote_per_county:.1f}% ({votes_county:,})")
    
        #Finding the county with the highest turnout
        if (votes_county > county_turnout) and (vote_per_county > county_turnout_percentage):
            county_turnout = votes_county
            county_turnout_percentage = vote_per_county
            winning_county = county_name

        print(f"{county_results}")
        #  Save the county results to our text file.
        txt_file.write(f"{county_results}\n")

    #Print the winning county        
    winning_county_summary = (
    f"\n-------------------------\n"
    f"Largest County Tournout: {winning_county}\n"
    f"-------------------------\n")
    print(winning_county_summary)
     # Save the winning candidate's results to the text file.
    txt_file.write(f"{winning_county_summary}\n")

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        #Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        #Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # To do: print out each candidate's name, vote count, and percentage of
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(f"{candidate_results}\n")

        if (votes > winning_count) and (winning_percentage < vote_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            #Set the winning_candidate equal to the candidate's name.
            winnnig_candidate  = candidate_name

    #Print the winning candidate        
    winning_candidate_summary = (
    f"\n-------------------------\n"
    f"Winner: {winnnig_candidate }\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
     # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)







        