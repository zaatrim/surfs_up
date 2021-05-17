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
        Insert Iamage1 

 In Part 2 of the analysis I will Use the code in part 1 and refactor it to run the analyisis om the of Decmber. 
         Insert Iamage 2
### Results

1) There are ~ 4 Degrees Difference between December and June. December stats are shifted by ~ 4 degrees ( Higher Degrees).
  a) Mean for Dec is 74.9 vs. 71.04 for June. 
2) Max temps in Dec are 83 vs. 85 during June. 
3) Have more Data for June Temp ( 1700) vs. December 1517.  
    
    
## *Summary*
By using SQLite & SQLAlchem, we could create local DB and queries to perform analysis. we could leverage this code to other Islands or different months during the year.  
 I can do the following additional analysis: 
  1) retrieve the precipitation scores for December & June and Run statistical analysis on Precipitation scores for Jun and December.   
      
       Insert Summary image1

  2) Evaluate the reliability of the Data source by check the sampling count per Station for Jun and December.
     
      Insert Summary image1
