import matplotlib.pyplot as plt

def hp_type_pie(calcs): # change the colors of the bar graph

    #grabbing data from database
    data = [calcs['percent_character_jokes'], calcs['percent_species_jokes'], calcs['percent_book_jokes']]

    #data for plotting
    colors = ['#740001','#D3A625','#5D5D5D',] # gryffindor color scheme
    myLabels = 'Characters', 'Species', 'Books'
    sizes = [round(float(data[0]),2), round(float(data[1]),2), round(float(data[2]),2)]
    stwing = [str(sizes[0]), str(sizes[1]), str(sizes[2])]
    label_string = [(stwing[0] + '%'), (stwing[1] + '%'), (stwing[2] + '%')]
    explode = (0, 0.1, 0)  

    #show the pie graph
    plt.pie(sizes, explode=explode, labels = label_string, colors = colors)
    plt.title('YoMama Jokes x Harry Potter Term Categories')
    plt.legend(myLabels,loc=2)
    plt.show()

def in_yomama_pie(calcs): # change the colors of the bar graph

    #grabbing data from database
    data = [calcs['percent_holiday_jokes'], calcs['percent_harry_jokes']]

    #data for plotting
    colors = ['#BCD687','#57A16D','#A13F3D'] # mixture of gryffindor / xmas colors 
    myLabels = 'Holiday Jokes in YoMama', 'Harry Potter Jokes in YoMama', 'Other in YoMama'
    other = 100 - (float(data[0])+ float(data[1]))
    sizes = [str(data[0]), str(data[1]), str(other)]
    label_string = [(sizes[0] + '%'), (sizes[1] + '%'), (sizes[2] + '%')]
    explode = (0, 0, 0.2)  

    #show the pie graph
    plt.pie(sizes, explode=explode, labels = label_string, colors = colors)
    plt.title('YoMama Jokes x Holiday and Harry Potter References x Other')
    plt.legend(myLabels,loc=2)
    plt.show()

def hp_vs_holiday_bar(calcs):
    data = [calcs['total_harry_jokes'], calcs['total_holiday_jokes']]
  
    # creating the dataset
    types = ['Harry Potter Terms', 'Holiday Terms']
    values = data

    fig, ax = plt.subplots(figsize =(5, 8))

    ax.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)
    
    # creating the bar plot
    plt.bar(types, values, color ='#946B2D',
            width = 0.5)
    
    plt.xlabel("APIs")
    plt.ylabel("No. of Terms in YoMama Jokes")
    plt.title("YoMama Jokes x Holiday and Harry Potter References")
    plt.show()
