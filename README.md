# H1b-analysis

# Problem
To create a mechanism to analyze past years data, specifically to calculate the required metrics: Top 10 occupations and Top 10 states for certified visa applications. Input folder consists of .csv file with required data and the output folder consists of .txt file with required results. And the code should be modular and reusable for future data.

# Approach
1. Read the input .csv file
2. Initialization of required lists and variables
3. Filtering the data in which the case status is certified
4. Counting the number of occurances of each state and also the number of occurances of each occupation
5. Arranging them in the required order
6. Calculating the percentage of each state compared to all certified cases and also percentage of each occupation comapared to all certified cases
7. Making combined list of occurances and perecntages
8. Saving the outputs into .txt files

# Run instructions
The following are the instructions to run the file:
1. Clone the folder $ git clone https://github.com/madhyasa/H1b-analysis.git
2. Open the h1b-analysis folder $ cd H1b-analysis
3. Run the python file with the following command and then check the ouput in output folder: $ python src/analysis.py input/h1b_input.csv output/top_10_occupations.txt output/top_10_states.txt
4. Now go to insight_testsuite folder to test the code $ cd insight_testsuite
5. To make script an executable program $ chmod +x run_tests.sh
6. To run the test cases $ ./run_tests.sh
