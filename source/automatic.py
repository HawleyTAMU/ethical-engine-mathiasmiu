from audit import audit

def automatic_decision(scenario):
    # *** YOUR CODE GOES HERE ***
    listPassengers = scenario.getPassengers()
    listPedestrians = scenario.getPedestrians()
    
    numPs = len(listPassengers)
    numPeds = len(listPedestrians)

    numPsDocs = 0
    numPedsDocs = 0

    if numPs > numPeds:
        return "passengers"
    elif numPs < numPeds:
        return "pedestrians"
    else:
        #find the number of doctors that are employed then if equal go to next tiebreaker
        for i in range(numPs):
            if listPassengers[i].getProfession() == "doctor":
                isHomeless = listPassengers[i].isHomeless()
                if not isHomeless:
                    numPsDocs += 1
        
        for i in range(numPeds):
            if listPedestrians[i].getProfession() == "doctor":
                isHomeless = listPedestrians[i].isHomeless()
                if not isHomeless:
                    numPedsDocs += 1
        
        if numPsDocs > numPedsDocs:
            return "passengers"
        elif numPsDocs < numPedsDocs:
            return "pedestrians"
        else:
            #find the number of pregnant women
            numPsPreg = 0
            numPedsPreg = 0

            for i in range(numPs):
                if listPassengers[i].isPregnant():
                    numPsPreg += 1

            for i in range(numPeds):
                if listPedestrians[i].isPregnant():
                    numPedsPreg += 1

            if numPsPreg > numPedsPreg:
                return "passengers"
            elif numPsPreg < numPedsPreg:
                return "pedestrians"
            else:
                            
                numPsCriminal = 0
                numPedsCriminal = 0

                for i in range(numPs):
                    if listPassengers[i].isCriminal():
                        numPsCriminal += 1

                for i in range(numPeds):
                    if listPedestrians[i].isCriminal():
                        numPedsCriminal += 1

                if numPsCriminal > numPedsCriminal:
                    return "passengers"
                elif numPsCriminal < numPedsCriminal:
                    return "pedestrians"
                else:
                    return "pedestrians"
            
            #after these tiebreakers, if still equal, default to saving the pedestrians since passenegers understand the risk assocaite with riding in a self driving car even if subconcious



    # default to saving the passengers
    return "passengers" 

if __name__ == '__main__':
    audit(automatic_decision, 60, seed=8675309)
