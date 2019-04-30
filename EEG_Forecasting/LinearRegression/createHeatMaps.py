import plotly.plotly as py
import plotly.figure_factory as ff

# heatMap is the to be saved numpy array of mean squared error 
# for different eeg and emg latencies
heatMap = np.load('latencyHeatmap.npy')
colorscale = [[0, '#66475e'], [1, '#ecbfe0']]
font_colors = ['#efecee', '#3c3636']
fig = ff.create_annotated_heatmap(heatMap, colorscale=colorscale, 
                                  font_colors=font_colors)
py.iplot(fig, filename='annotated_heatmap_custom_color')