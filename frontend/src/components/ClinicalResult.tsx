import {
    AlertTriangle,
    BookOpen,
    FileText,
    UserRound,
    Database,
    Activity
} from "lucide-react";


interface Props {

    result:any;

}



function ClinicalResult({

    result

}:Props){


    return (

        <div className="space-y-6">


            {/* AI Status Header */}

            <div className="
                flex
                flex-col
                sm:flex-row
                sm:items-center
                sm:justify-between
                gap-4
                bg-blue-50
                border
                border-blue-200
                rounded-2xl
                p-5
            ">


                <div className="flex items-center gap-3">


                    <Activity
                        className="text-blue-700"
                        size={28}
                    />


                    <div>


                        <h3 className="
                            text-lg
                            font-bold
                            text-slate-800
                        ">

                            AI Clinical Assessment Complete

                        </h3>


                        <p className="
                            text-sm
                            text-slate-600
                        ">

                            Multi-agent clinical reasoning workflow

                        </p>


                    </div>


                </div>



                <div className="
                    bg-red-100
                    text-red-700
                    px-4
                    py-2
                    rounded-full
                    font-semibold
                    text-sm
                    flex
                    items-center
                    gap-2
                ">


                    <AlertTriangle size={18}/>


                    Review Required


                </div>


            </div>





            {/* Patient Information */}

            <ResultCard

                title="Patient Information"

                icon={
                    <UserRound
                        className="text-blue-600"
                    />
                }

                style="bg-slate-50 border-slate-200"

                content={result.patient_information}

            />





            {/* Clinical Facts */}

            <ResultCard

                title="Verified Clinical Data"

                icon={
                    <Database
                        className="text-green-600"
                    />
                }

                style="bg-green-50 border-green-200"

                content={result.clinical_facts}

            />






            {/* Triage */}

            <ResultCard

                title="Triage Assessment"

                icon={
                    <AlertTriangle
                        className="text-red-600"
                    />
                }

                style="bg-red-50 border-red-200"

                content={result.triage_result}

            />






            {/* Knowledge */}

            <ResultCard

                title="Clinical Knowledge Support"

                icon={
                    <BookOpen
                        className="text-blue-600"
                    />
                }

                style="bg-blue-50 border-blue-200"

                content={result.knowledge_result}

            />






            {/* Clinical Note */}

            <ResultCard

                title="Generated Clinical Note"

                icon={
                    <FileText
                        className="text-purple-600"
                    />
                }

                style="bg-purple-50 border-purple-200"

                content={result.clinical_note}

            />


        </div>

    )

}





function ResultCard({

    title,

    icon,

    content,

    style

}:{

    title:string;

    icon:any;

    content:string;

    style:string;

}){


    return (

        <div className={`
            ${style}
            border
            rounded-2xl
            p-5
            shadow-sm
        `}>


            <div className="
                flex
                items-center
                gap-3
                mb-4
            ">


                {icon}


                <h3 className="
                    text-lg
                    font-semibold
                    text-slate-800
                ">

                    {title}

                </h3>


            </div>




            <div className="
                bg-white
                rounded-xl
                p-4
                border
                border-slate-200
                max-h-[500px]
                overflow-y-auto
            ">


                <pre className="
                    whitespace-pre-wrap
                    text-sm
                    leading-relaxed
                    text-slate-700
                    font-sans
                ">

                    {content || "Not available"}

                </pre>


            </div>


        </div>

    )

}



export default ClinicalResult;