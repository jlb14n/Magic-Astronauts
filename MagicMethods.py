#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Part2: Create an Astronaut Object
class Astronaut:
    """Astronaut class"""
    def __init__(self,name,status,space_flight_hr):
        self.__name=name
        self.__status=status
        self.__space_flight_hr=space_flight_hr
    
    @property
    def name(self):
        return self.__name

    @property
    def status(self):
        return self.__status

    @property
    def space_flight_hr(self):
        return self.__space_flight_hr

    @property
    def year(self):
        return self.__year    

    @property
    def group(self):
        return self.__group

    @property
    def birth_date(self):
        return self.__birth_date

    @property
    def birth_place(self):
        return self.__birth_place

    @property
    def gender(self):
        return self.__gender

    @property
    def alma_mater(self):
        return self.__alma_mater
        
    @property
    def undergraduate_major(self):
        return self.__undergraduate_major

    @property
    def graduate_major(self):
        return self.__graduate_major  

    @property
    def military_rank(self):
        return self.__military_rank

    @property
    def military_branch(self):
        return self.__military_branch

    @property
    def is_military_retired(self):
        return self.__is_military_retired

    @property
    def space_flights(self):
        return self.__space_flights

    @property
    def space_walks(self):
        return self.__space_walks

    @property
    def space_walks_hr(self):
        return self.__space_walks_hr

    @property
    def space_flight_hr(self):
        return self.__space_flight_hr

    @property
    def missions(self):
        return self.__missions

    @property
    def death_date(self):
        return self.__death_date

    @property
    def death_mission(self):
        return self.__death_mission

    @name.setter
    def name(self,new_name):
        self.__name=new_name

    @status.setter
    def status(self,new_status):
        self.__status=new_status
    
    @space_flight_hr.setter
    def space_flight_hr(self,new_space_flight_hr):
        self.__space_flight_hr=new_space_flight_hr
    
    @year.setter
    def year(self,new_year):
        self.__year=new_year

    @group.setter
    def group(self,new_group):
        self.__group=new_group

    @birth_date.setter
    def birth_date(self,new_birth_date):
        self.__birth_date=new_birth_date

    @birth_place.setter
    def birth_place(self,new_birth_place):
        self.__birth_place=new_birth_place

    @gender.setter
    def gender(self,new_gender):
        self.__gender=new_gender

    @alma_mater.setter
    def alma_mater(self,new_alma_mater):
        self.__alma_mater=new_alma_mater

    @undergraduate_major.setter
    def undergraduate_major(self,new_undergraduate_major):
        self.__undergraduate_major=new_undergraduate_major
        
    @graduate_major.setter
    def graduate_major(self,new_graduate_major):
        self.__graduate_major=new_graduate_major

    @military_rank.setter
    def military_rank(self,new_military_rank):
        self.__military_rank=new_military_rank

    @military_branch.setter
    def military_branch(self,new_military_branch):
        self.__military_branch=new_military_branch

    @is_military_retired.setter
    def is_military_retired(self,new_is_military_retired):
        self.__is_military_retired=new_is_military_retired

    @space_flights.setter
    def space_flights(self,new_space_flights):
        self.__space_flights=new_space_flights

    @space_flight_hr.setter
    def space_flight_hr(self,new_space_flight_hr):
        self.__space_flight_hr=new_space_flight_hr

    @space_walks.setter
    def space_walks(self,new_space_walks):
        self.__space_walks=new_space_walks

    @space_walks_hr.setter
    def space_walks_hr(self,new_space_walks_hr):
        self.__space_walks_hr=new_space_walks_hr

    @missions.setter
    def missions(self,new_missions):
        self.__missions=new_missions

    @death_date.setter
    def death_date(self,new_death_date):
        self.__death_date=new_death_date

    @death_mission.setter
    def death_mission(self,new_death_mission):
        self.__death_mission=new_death_mission

    def __gt__(self,other):
        return self.space_flight_hr>other.space_flight_hr

    def __ge__(self,other):
        return self.space_flight_hr>=other.space_flight_hr
    
    def __eq__(self,other):
        return self.space_flight_hr==other.space_flight_hr
    
    def __str__(self):
        return self.__name+", "+self.__status
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Part3: Create a List of Astronaut Objects
import csv
import random
with open("astronauts.csv", newline='') as csvfile:
    astro_list=[{x.lower().replace(' ','_').replace('(','').replace(')',''):y for x,y in row.items()} for row in csv.DictReader(csvfile)]
astro_objects=[]
for astronaut in astro_list:
    astro_objects.append(Astronaut(astronaut['name'],astronaut['status'],astronaut['space_flight_hr']))

#List all the mutable properties for the first astronaut object.
print(astro_objects[0].__dict__)

#Pick two random Astronaut objects and compare them based on Flight(hrs).
ran_astro_1=astro_objects[random.randint(0,len(astro_objects)-1)]
ran_astro_2=astro_objects[random.randint(0,len(astro_objects)-1)]
print(f"{ran_astro_1} > {ran_astro_2}: {ran_astro_1 > ran_astro_2}")
print(f"{ran_astro_1} = {ran_astro_2}: {ran_astro_1 == ran_astro_2}")
print(f"{ran_astro_1} >= {ran_astro_2}: {ran_astro_1 >= ran_astro_2}")

#Print out all astronauts from the astronaut list.
[print(astronaut) for astronaut in astro_objects]