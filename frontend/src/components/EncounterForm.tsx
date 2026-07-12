import {useState} from "react";
import api from "../services/api";


interface Props{

    patientId:string;

    onResult:(data:any)=>void;

}



function EncounterForm({
    patientId,
    onResult
}:Props){


    const [symptoms,setSymptoms]=useState("");



    async function runWorkflow(){


        const response = await api.post(
            "/clinical/workflow",
            {

                patient_id:Number(patientId),

                symptoms:symptoms

            }
        );


        onResult(response.data);


    }




    return (

        <div>


            <h2>
                New Clinical Encounter
            </h2>


            <textarea

                placeholder="Enter symptoms"

                value={symptoms}

                onChange={
                    e=>setSymptoms(e.target.value)
                }

            />


            <br/>


            <button
                onClick={runWorkflow}
            >

                Run Clinical AI

            </button>


        </div>

    )

}


export default EncounterForm;