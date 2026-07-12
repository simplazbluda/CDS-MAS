import { useState } from "react";


function PatientForm(){

    const [patientId,setPatientId] = useState("");



    return (

        <div>

            <h2>
                Patient Selection
            </h2>


            <input
                placeholder="Patient ID"
                value={patientId}
                onChange={
                    e=>setPatientId(e.target.value)
                }
            />


        </div>

    )

}


export default PatientForm;