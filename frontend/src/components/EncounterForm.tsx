import { useState } from "react";

import {
    BrainCircuit,
    LoaderCircle,
    Activity
} from "lucide-react";

import api from "../services/api";


interface Props {

    patientId: string;

    onResult: (data:any)=>void;

}


function EncounterForm({

    patientId,

    onResult

}:Props){


    const [symptoms,setSymptoms] = useState("");

    const [loading,setLoading] = useState(false);



    async function runWorkflow(){


        if(!symptoms.trim()){

            alert(
                "Please enter patient symptoms."
            );

            return;

        }



        try{


            setLoading(true);



            const response = await api.post(

                "/clinical/workflow",

                {

                    patient_id:Number(patientId),

                    symptoms:symptoms

                }

            );


            onResult(response.data);



        }

        catch(error){

            console.error(error);


            alert(
                "Unable to run clinical workflow."
            );

        }

        finally{

            setLoading(false);

        }


    }



    return (

        <div className="space-y-5">


            {/* Symptoms Input */}

            <div>


                <label

                    className="
                    flex
                    items-center
                    gap-2
                    text-sm
                    font-semibold
                    text-slate-700
                    mb-3
                    "

                >

                    <Activity
                        size={18}
                        className="text-blue-600"
                    />

                    Patient Symptoms

                </label>



                <textarea


                    className="
                    w-full
                    min-h-[160px]
                    rounded-xl
                    border
                    border-slate-300
                    bg-slate-50
                    p-4
                    text-slate-800
                    placeholder:text-slate-400
                    shadow-sm
                    resize-none
                    focus:outline-none
                    focus:ring-4
                    focus:ring-blue-100
                    focus:border-blue-600
                    transition
                    "


                    placeholder="
Example:
- Severe headache
- Fever
- Chest pain
- Fatigue
- Shortness of breath
                    "



                    value={symptoms}



                    onChange={

                        e =>
                        setSymptoms(
                            e.target.value
                        )

                    }


                />

            </div>





            {/* Run AI Button */}


            <button


                onClick={runWorkflow}


                disabled={loading}



                className="

                w-full
                sm:w-auto

                flex
                items-center
                justify-center

                gap-3

                bg-blue-700

                text-white

                font-semibold

                px-8

                py-3

                rounded-xl

                shadow-md

                hover:bg-blue-800

                hover:shadow-lg

                disabled:bg-slate-400

                disabled:cursor-not-allowed

                transition-all

                "


            >


                {

                    loading

                    ?

                    <>

                    <LoaderCircle

                        className="animate-spin"

                        size={22}

                    />

                    Running AI Analysis...

                    </>


                    :

                    <>

                    <BrainCircuit

                        size={22}

                    />

                    Run Clinical AI

                    </>


                }


            </button>



            {

                loading &&

                <div

                    className="
                    flex
                    items-center
                    gap-2
                    text-sm
                    text-blue-600
                    bg-blue-50
                    rounded-lg
                    p-3
                    "

                >

                    <LoaderCircle

                        className="animate-spin"

                        size={16}

                    />

                    Clinical agents are analysing patient information...

                </div>


            }



        </div>

    );


}


export default EncounterForm;