install.packages("xml2")
install.packages("rvest")
install.packages("stringr")
library(xml2)
library(rvest)
library(stringr)
library(dplyr)
library(lubridate)

##Baden Wurttemberg
Baden_Wurttemberg <- "https://de.fuelo.net/gasstations/province/113?lang=en"

Baden_Wurttemberg_Data <- Baden_Wurttemberg %>%
  html() %>%
  html_nodes(xpath='/html/body/div[1]/div[4]/div/div[1]/div[2]/div[2]/table') %>%
  html_table()


Baden_Wurttemberg_Data <- Baden_Wurttemberg_Data[[1]]
Esso_Baden_Wurttemberg <- Baden_Wurttemberg_Data %>% select(Name) %>% filter(grepl("Esso", Name))
#Baden Wurttemberg: 195 Esso Stations

Bavaria <- "https://de.fuelo.net/gasstations/province/114?lang=en"

Bavaria_Data <- Bavaria %>%
  html() %>%
  html_nodes(xpath='/html/body/div[1]/div[4]/div/div[1]/div[2]/div[2]/table') %>%
  html_table()

Bavaria_Data <- Bavaria_Data[[1]]
Esso_Bavaria_Data <- Bavaria_Data %>% select(Name) %>% filter(grepl("Esso", Name))
#Bavaria: 187 Esso Stations



##Berlin
Berlin <- "https://de.fuelo.net/gasstations/province/115?lang=en"

Berlin_Data <- Berlin %>%
  html() %>%
  html_nodes(xpath='/html/body/div[1]/div[4]/div/div[1]/div[2]/div[2]/table') %>%
  html_table()

Berlin_Data <- Berlin_Data[[1]]
Esso_Berlin_Data <- Berlin_Data %>% select(Name) %>% filter(grepl("Esso", Name))
#Berlin: 28 Esso Stations

##Brandenburg
Brandenburg <- "https://de.fuelo.net/gasstations/province/116?lang=en"

Brandenburg_Data <- Brandenburg %>%
  html() %>%
  html_nodes(xpath='/html/body/div[1]/div[4]/div/div[1]/div[2]/div[2]/table') %>%
  html_table()

Brandenburg_Data <- Brandenburg_Data[[1]]
Esso_Brandenburg_Data <- Brandenburg_Data %>% select(Name) %>% filter(grepl("Esso", Name))
#Brandenburg: 23 Esso Gas Stations


#Bremen
Bremen <- "https://de.fuelo.net/gasstations/province/117?lang=en"

Bremen_Data <- Bremen %>%
  html() %>%
  html_nodes(xpath='/html/body/div[1]/div[4]/div/div[1]/div[2]/div[2]/table') %>%
  html_table()

Bremen_Data <- Bremen_Data[[1]]
Esso_Bremen_Data <- Bremen_Data %>% select(Name) %>% filter(grepl("Esso", Name))
#Bremen: 9 Esso Gas Stations

##Hamburg
Hamburg <- "https://de.fuelo.net/gasstations/province/118?lang=en"

Hamburg_Data <- Hamburg %>%
  html() %>%
  html_nodes(xpath='/html/body/div[1]/div[4]/div/div[1]/div[2]/div[2]/table') %>%
  html_table()

Hamburg_Data <- Hamburg_Data[[1]]
Esso_Hamburg_Data <- Hamburg_Data %>% select(Name) %>% filter(grepl("Esso", Name))
##Hamburg: 27 Esso Gas Stations

#Hesse 

Hesse <- "https://de.fuelo.net/gasstations/province/119?lang=en"

Hesse_Data <- Hesse %>%
  html() %>%
  html_nodes(xpath='/html/body/div[1]/div[4]/div/div[1]/div[2]/div[2]/table') %>%
  html_table()

Hesse_Data <- Hesse_Data[[1]]
Esso_Hesse_Data <- Hesse_Data %>% filter(grepl("Esso", Name))
#Hesse: 110 Esso Gas Stations

Mecklenburg <- "https://de.fuelo.net/gasstations/province/120?lang=en"

Mecklenburg_Data <- Mecklenburg %>%
  html() %>%
  html_nodes(xpath='/html/body/div[1]/div[4]/div/div[1]/div[2]/div[2]/table') %>%
  html_table()

Mecklenburg_Data <- Mecklenburg_Data[[1]]
Esso_Mecklenburg_Data <- Mecklenburg_Data %>% select(Name) %>% filter(grepl("Esso", Name))
#Mecklenburg: 28 Esso Gas Stations


##Lower Saxony

LSaxony <- "https://de.fuelo.net/gasstations/province/121?lang=en"

LSaxony_Data <- Saxony %>%
  html() %>%
  html_nodes(xpath='/html/body/div[1]/div[4]/div/div[1]/div[2]/div[2]/table') %>%
  html_table()

LSaxony_Data <- LSaxony_Data[[1]]
Esso_LSaxony_Data <- LSaxony_Data %>% select(Name) %>% filter(grepl("Esso", Name))
##Lower Saxony: 133 Esso Gas Stations


##North-Rhine
Rhine <- "https://de.fuelo.net/gasstations/province/122?lang=en"

Rhine_Data <- Rhine %>%
  html() %>%
  html_nodes(xpath='/html/body/div[1]/div[4]/div/div[1]/div[2]/div[2]/table') %>%
  html_table()

Rhine_Data <- Rhine_Data[[1]]
Esso_Rhine_Data <- Rhine_Data %>% select(Name) %>% filter(grepl("Esso", Name))
#Rhine: 191 Esso Gas Stations

##Rhineland-Palatinate

Palatinate <- "https://de.fuelo.net/gasstations/province/123?lang=en"

Palatinate_Data <- Palatinate %>%
  html() %>%
  html_nodes(xpath='/html/body/div[1]/div[4]/div/div[1]/div[2]/div[2]/table') %>%
  html_table()

Palatinate_Data <- Palatinate_Data[[1]]
Esso_Palatinate_Data <- Palatinate_Data %>% select(Name) %>% filter(grepl("Esso", Name))
#Palatinate: 62 Esso Gas Stations


## Saarland

Saarland <-"https://de.fuelo.net/gasstations/province/124?lang=en"

Saarland_Data <- Saarland %>%
  html() %>%
  html_nodes(xpath="/html/body/div[1]/div[4]/div/div[1]/div[2]/div[2]/table") %>%
  html_table()

Saarland_Data <- Saarland_Data[[1]]
Esso_Saarland_Data <-Saarland_Data %>% select(Name) %>% filter(grepl("Esso", Name))
##Saarland: 13 Esso Stations


##Saxony

Saxony <- "https://de.fuelo.net/gasstations/province/125?lang=en"

Saxony_Data <- Saxony %>%
  html() %>%
  html_nodes(xpath='/html/body/div[1]/div[4]/div/div[1]/div[2]/div[2]/table') %>%
  html_table()

Saxony_Data <- Saxony_Data[[1]]

Esso_Saxony_Data <-Saxony_Data %>% select(Name) %>% filter(grepl("Esso", Name))
#Saxony: 34 Esso Gas Stations


##Saxony_Anhalt

Anhalt <- "https://de.fuelo.net/gasstations/province/126?lang=en"

Anhalt_Data <- Anhalt %>%
  html() %>%
  html_nodes(xpath='/html/body/div[1]/div[4]/div/div[1]/div[2]/div[2]/table') %>%
  html_table()

Anhalt_Data <-Anhalt_Data[[1]]
Esso_Anhalt_Data <- Anhalt_Data %>% select(Name) %>% filter(grepl("Esso", Name))
##Anhalt: 23 Esso Gas Sations



##Schleswig-Holstein

Schleswig <- "https://de.fuelo.net/gasstations/province/127?lang=en"

Schleswig_Data <- Schleswig %>%
  html() %>%
  html_nodes(xpath='/html/body/div[1]/div[4]/div/div[1]/div[2]/div[2]/table') %>%
  html_table()

Schleswig_Data <- Schleswig_Data[[1]]
Esso_Schleswig_Data <- Schleswig_Data %>% select(Name) %>% filter(grepl("Esso", Name))
##Scheswig: 35 Esso Gas Stations


##Thuringia

Thuringia <- "https://de.fuelo.net/gasstations/province/128?lang=en"

Thuringia_Data <- Thuringia %>%
  html() %>%
  html_nodes(xpath='/html/body/div[1]/div[4]/div/div[1]/div[2]/div[2]/table') %>%
  html_table()

Thuringia_Data <- Thuringia_Data[[1]]
Esso_Thuringia_Data <- Thuringia_Data %>% select(Name) %>% filter(grepl("Esso", Name))
#Thuringia: 17 Esso Gas Stations
