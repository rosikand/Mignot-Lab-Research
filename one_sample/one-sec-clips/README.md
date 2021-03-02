# One second clips

This is an experiment where each audio sample is one second long instead of ten. The labelling process was the roughly the same. The classes were balanced out such that they contain the same number of samples per class. 

## Notebooks:

- `data_analysis.ipynb`: this notebook displays three samples from each class along with their corresponding Mel Spectrograms and Waveforms. 
- `lstm_num_one.ipynb`: this notebook contains training and testing an LSTM model on this data. Performance metrics from predictions on the test set are also shown (as with all model notebooks below). Training was done for 250 epochs. 'num_one' means this was the first run of that LSTM model. 
- `lstm_num_two.ipynb`: same as `lstm_num_one.ipynb` except trained for 2500 epochs. 
- `fc_num_one.ipynb`: fully-connected dense linear model trained for 250 epochs. 
- `fc_num_two.ipynb`: fully-connected dense linear model trained for 1000 epochs.
