from os import name
from app import app
from app.blockchain import BlockChain
from flask import render_template
from flask import request, redirect

# render_template("index.html")

bc = BlockChain()
nonceList = []
transaction = {}

@app.route("/", methods=["GET", "POST"])
def index():
    
    # print(f"on indexRoute bc: {bc.blocks}")
    # print(f"on indexRoute bc.currentNonce: {bc.currentNonce}")
    # print(f"on indexRoute nonceList: {nonceList}")

    if request.method == "POST":

        req = request.form
        
        # iterate through the keys and values of our req object and look for missing fields        
        missing = list()

        for k, v in req.items():
            if v == "":
                missing.append(k)

        if missing:
            feedback = f"Missing fields for {', '.join(missing)}"
            return render_template("index.html", feedback=feedback, nonceList=nonceList)
        else:
            runOnPostdata(req)
        

        return redirect(request.url)

    return render_template("index.html", nonceList=nonceList)



def runOnPostdata(requestDict):
    print(f"----- runOnPostdata -------")
    
    spendenTyp      = requestDict["spenden_typ"]
    betrag          = float(requestDict["betrag"])
    spendenBetrag   = 0
    
    # Abfrage und entsprechende Berechnung der Spende 
    if spendenTyp=="prozent":
        
        spendenBetrag = betrag * 0.05
        # print(f"spendenBetrag - 5%: {spendenBetrag}")
        
    elif spendenTyp=="fix":
        
        spendenBetrag = 5
        # print(f"spendenBetrag - 5: {spendenBetrag}")
        
    else:
        return
    
    # betrag neu berechnen 
    betrag -= spendenBetrag
    
    # fill transaction with calculated and received data from our form 
    transaction = {
        'name':     requestDict['name'],
        'betrag':   betrag,
        'spende':   spendenBetrag,
    }
        
    # add a new transaction aka a new block to our blockchain 
    bc.append(transaction)
    
    # add the nonce of this block to our list 
    nonceList.append(bc.currentNonce)
    
    
    print(f"> added a new block: {bc.blocks}")
    # print(f"on PostData nonceList: {nonceList}")
    print(f"----- end runOnPostdata -------")
        
    


    
    