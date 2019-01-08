import sys, os


def main(argv):

	if len(argv) != 2:
		print("Usage: python comparetogold.py <input_folder> <gold_file>")
		sys.exit(2)


	inputfolder = argv[0]
	goldfile = argv[1]
	
	os.chdir(inputfolder)
	directory = os.fsencode(os.getcwd())

	basemodel_acc_sum = 0
	n_basemodels = 0

	# Create 'accuracies' directory if doesn't already exist
	output_dir = 'accuracies'

	if not os.path.exists(output_dir):
		os.mkdir(output_dir)
		print("Directory '" + output_dir + "' was created.\n")
	else:
		print("Directory '" + output_dir + "' already exists.\n")
		

	with open(output_dir+'/all_accuracies.txt', 'w') as all_accuracies:
		print("All accuracies:\n\n{:<40}{:<40}\n".format("File", "Accuracy"), file=all_accuracies)
		for file in os.listdir(directory):
			linecount = 0
			filename = os.fsdecode(file)
			outfilename = output_dir+"/"+filename+"_-_VS_-_"+goldfile

			if not filename.endswith("gold.txt") and not os.path.isdir(filename):
				try:
					with open(filename, 'r') as pred, open(goldfile, 'r') as gold, open(outfilename, 'w') as outfile:

						print("Input files:\npred: "+filename+"\ngold: "+goldfile, file=outfile)
						print("\n\nWrong predictions:\n", file=outfile)
						n_wrong = 0
						
						for line1, line2 in zip(pred, gold):
							linecount += 1
							if line1 != line2:
								n_wrong += 1
								print("\n{}:\n{:<12} {}\n{:<12} {}"\
									  .format(n_wrong, "Predicted:", line1.strip("\n"), "Gold:", line2).strip("\n"),\
									  end="\n\n", file=outfile)

						accuracy = ((linecount-n_wrong) / linecount) * 100
						percentage = str(accuracy)+"%"

						if filename.startswith("pred_"):
							basemodel_acc_sum += accuracy
							n_basemodels += 1

						outfile.write("\n--------------------------------\n\nAccuracy: "+percentage)
						print("File: {:<40}Accuracy: {:<40}".format(filename, percentage))
						print("{:<40}{:<40}".format(filename, accuracy), file=all_accuracies)

				except Exception as e: print(e)


		avg_accuracy = str(basemodel_acc_sum / n_basemodels)
		print("\n{:<40}{:<40}".format("Average accuracy of baseline models:", avg_accuracy), file=all_accuracies)
		print("\n{:<56}{:<16}".format("Average accuracy of baseline models (s1-s10): ", avg_accuracy+"%"))

if __name__ == "__main__":
   main(sys.argv[1:])