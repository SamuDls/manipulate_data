import matplotlib.pyplot as plt

def create_bar_chart(labels,values):
   fig, ax = plt.subplots()
   fig.set_facecolor("black")
   ax.bar(labels,values)
   plt.show()


def create_pie_chart(labels,values):
   fig,ax = plt.subplots()
   ax.pie(values, labels =labels)
   ax.axis("equal")
   plt.show()

if __name__=="__main__":
   labels =["rojo","perro","color","nombre"]
   values = [1,44,55,92]
   create_pie_chart(labels ,values)