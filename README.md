# surfs_up

## *Project Overview*
Our objective in this Analysis is to help W.Avy to show the board of Directors the Potential of a Surfing /ice cream shop throughout the year. To show the potential, I will run a statistical analysis of temperature during Jun & December. To run this analysis, I will Use Python Pandas, Numpy, SQLite & SQLAlchemy   
                    
## *Analysis & Results*
### Analysis
1st step in this analysis is to import all dependencies; NumPy, pandas & SQLAlchemy
next, I will create the path, Base, reference to each table & session: 

        engine = create_engine("sqlite:///hawaii.sqlite")
        Base = automap_base()
        Base.prepare(engine, reflect=True)
        Measurement = Base.classes.measurement
        Station = Base.classes.station
        session = Session(engine)


part 1 of the analysis will focus on June: I will extract the temperature Data for June and then run a statistical analysis to check the Average, Min, and Max temperatures. as well will calculate the Standard deviation and the quartiles. I will follow the following steps  :
    1) Write a query that filters the Measurement table to retrieve the temperatures for June
            
            june_temp = session.query(Measurement.date, Measurement.tobs).filter(extract("month", Measurement.date) == 6).all()
            
   2) Convert the June temperatures to a list.
  
            june_temp_list= list (june_temp)
   3) Create a DataFrame from the list of temperatures for June. 
  
            june_df = pd.DataFrame(june_temp_list, columns=['date','June Temps']) 
   4) The final step to Calculate and print out the summary statistics for the June temperature DataFrame. 
  
            june_df.describe()
            
   ![june_temp](https://user-images.githubusercontent.com/80013773/118435603-1f364f00-b694-11eb-8d85-ecec5a3d6e3c.PNG)

 In Part 2 of the analysis I will Use the code in part 1 and refactor it to run the analyisis om the of Decmber. 
 
   ![Dec_Temp](https://user-images.githubusercontent.com/80013773/118436075-f95d7a00-b694-11eb-8134-b70ec666c02c.PNG)

### Results

1) There are ~ 4 Degrees Difference between December and June. December stats are shifted by ~ 4 degrees ( Higher Degrees).
  a) Mean for Dec is 74.9 vs. 71.04 for June. 
2) Max temps in Dec are 83 vs. 85 during June. 
3) Have more Data for June Temp ( 1700) vs. December 1517. 
 
 ![juneDectemp](https://user-images.githubusercontent.com/80013773/118436178-31fd5380-b695-11eb-9e0e-ff1c89ae212e.png)
## *Summary*
By using SQLite & SQLAlchem, we could create local DB and queries to perform analysis. we could leverage this code to other Islands or different months during the year.  
 I can do the following additional analysis: 
  1) retrieve the precipitation scores for December & June and Run statistical analysis on Precipitation scores for Jun and December.   
      
  ![Summary image1](https://user-images.githubusercontent.com/80013773/118436227-4c373180-b695-11eb-83da-666da0f356f5.PNG)

  2) Evaluate the reliability of the Data source by check the sampling count per Station for Jun and December.
     
  ![Summary image2](https://user-images.githubusercontent.com/80013773/118436275-6709a600-b695-11eb-84a7-dfdef468c065.PNG)
