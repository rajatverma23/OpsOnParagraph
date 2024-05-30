import os
import string
import matplotlib.pyplot as plt

folder_path = '/Users/Nikita/beyatch/Projects/BharatGPT/untitled folder 2/'
max_files = 10
step_size = 2

data = {'File': [], 'Word Count': []}

for foldername, subfolders, files in os.walk(folder_path):
    for filename in files[:max_files]:  
        filepath = os.path.join(foldername, filename)

        try:
            with open(filepath, 'r', encoding='utf-8') as fp:
                print(f'Processing file: {filepath}')

                word_counts = []
                len_of_words = 0
                no_of_lines = 0

                for line in fp:
                    remove_punctuation = str.maketrans("", "", string.punctuation + '।,')
                    words = line.translate(remove_punctuation).split()

                    len_of_words = len_of_words + len(words)
                    no_of_lines = no_of_lines + 1;
        	
        	words_per_line = int(len_of_words/no_of_lines);

                data['File'].append(filename)
		data['Word Count'].extends(words_per_line)
        except Exception as e:
            print(f'Error processing file {filepath}: {e}')

plt.hist(data['Word Count'], bins=range(min(data['Word Count']), max(data['Word Count']) + step_size, step_size), edgecolor='black', stacked=True)
plt.title('Combined Histogram of Words per Line')
plt.xlabel('Number of Words')
plt.ylabel('Frequency of lines')

plt.xticks(range(0, 30 + step_size, step_size))

plt.show()
