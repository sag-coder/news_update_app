from tkinter import *
import requests


class News:

	def __init__(self):

		self.root=Tk()



		self.root.title("News Application")
		self.root.minsize(300,400)
		self.root.maxsize(300,400)

		self.root.configure(background="#E56134")
		self.main_window()
		self.root.mainloop()

	def clear(self):
			for i in self.root.pack_slaves():
					i.destroy()

	def main_window(self):
		self.clear()

		self.label=Label(self.root, text="News 24x7",bg="#E56134",fg="#fff")
		self.label.configure(font=("",25,"bold"))
		self.label.pack(pady=(40,60))

		self.label1=Label(self.root,text="Enter the topic", bg="#E56134", fg="#fff")
		self.label1.configure(font=("",12,""))
		self.label1.pack(pady=(10,5))

		self.topic=Entry(self.root)
		self.topic.pack(pady=(0,10),ipadx=30,ipady=3)

		self.click=Button(self.root, text="Search",bg="#fff",fg="#E56134",height="2",width="10",command= lambda: self.search_extraction())
		self.click.pack(pady=(10,10))
	
	def search_extraction(self):
		search=self.topic.get()
		self.data_handled(search)
	
	
	def data_handled(self,search):
		url="https://newsapi.org/v2/everything?q={}&apiKey=afa9526381204d1f8d02d8c6ee6c1742".format(search)
	
		response=requests.get(url)
		response=response.json()
		# self.data_organizer(response)
		self.data_organizer(response)
		

	
	def data_organizer(self,response):
		self.data_list=[]
		data=response['articles']
		for i in data:
			self.data_list.append(i)
		#print(self.data_list)
		self.data_store(index=0)
		
	def data_store(self,index):
		self.newsfeed(self.data_list[index],index=index)
	
	def newsfeed(self,data,index=None):
		self.clear()
		#display image
		print(data)
		#display title
		title=Label(self.root,text=data['title'])
		title.configure(font=("",10,""))
		title.pack(pady=(0,10))

	
		#content
		content=Label(self.root,text=data['content'])
		content.configure(font=("",10,""))
		content.pack(pady=(0,10))
		content["padx"]=50
		content['relief']="ridge"

		#button
		frame=Frame(self.root)
		frame.pack()
		if index>0:
			Button(frame,text="previous", command = lambda : self.data_store(index-1)).pack(side="left")
		if index!=19:
			Button(frame,text="next",command = lambda : self.data_store(index+1)).pack(side="left")
		

obj=News()