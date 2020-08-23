for lang in arabic finnish georgian german hindi italian khaling navajo russian turkish; do
    for file in ../accuracies_and_translate_results/"$lang"_accuracies_and_translate_results/accuracies/*; do
        if [[ $(basename "$file") == all_accuracies* ]] ; then
            echo "$file"
            cat ../accuracies_and_translate_results/"$lang"_accuracies_and_translate_results/accuracies/all_accuracies.txt | grep -o "base.txt\s\+[0-9\.]\+" | grep -o "[0-9\.]\+$" > "$lang"_pred_accuracies
            cat ../accuracies_and_translate_results/"$lang"_accuracies_and_translate_results/accuracies/all_accuracies.txt | grep -o "base_voted.txt\s\+[0-9\.]\+" | grep -o "[0-9\.]\+$" > "$lang"_voted_accuracy
            cat ../accuracies_and_translate_results/"$lang"_accuracies_and_translate_results/accuracies/all_accuracies.txt | grep -o "weighted_voted.txt\s\+[0-9\.]\+" | grep -o "[0-9\.]\+$" > "$lang"_weighted_voted_accuracy
        fi
    done
done