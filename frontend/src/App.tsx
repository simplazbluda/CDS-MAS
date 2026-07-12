import {useState} from "react";

import EncounterForm from "./components/EncounterForm";

import ClinicalResult from "./components/ClinicalResult";


function App(){


const [patientId,setPatientId]=useState("");

const [result,setResult]=useState<any>(null);



return (

<div>


<h1>
Medical AI Clinical Assistant
</h1>


<input

placeholder="Patient ID"

value={patientId}

onChange={
e=>setPatientId(e.target.value)
}

/>


<br/><br/>


{
patientId &&

<EncounterForm

patientId={patientId}

onResult={setResult}

/>

}



{
result &&

<ClinicalResult

result={result}

/>

}



</div>


)


}


export default App;