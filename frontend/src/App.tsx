import { useState } from "react";

import {
  Stethoscope,
  UserRound,
  ShieldCheck
} from "lucide-react";

import EncounterForm from "./components/EncounterForm";
import ClinicalResult from "./components/ClinicalResult";

function App() {

  const [patientId, setPatientId] = useState("");
  const [result, setResult] = useState<any>(null);

  return (

    <div className="min-h-screen bg-gradient-to-br from-slate-100 via-blue-50 to-white">

      {/* ===========================
          Header
      ============================ */}

      <header className="bg-blue-700 text-white shadow-lg">

        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-6 flex items-center gap-4">

          <div className="bg-white/20 p-3 rounded-xl">

            <Stethoscope size={34} />

          </div>

          <div>

            <h1 className="text-2xl sm:text-3xl lg:text-4xl font-bold">

              MedicalAI Clinical Assistant

            </h1>

            <p className="text-sm sm:text-base text-blue-100 mt-1">

              AI-powered Clinical Decision Support System

            </p>

          </div>

        </div>

      </header>

      {/* ===========================
          Main Content
      ============================ */}

      <main className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-6">

        {/* ===========================
            Patient Selection
        ============================ */}

        <section className="bg-white rounded-2xl shadow-md border border-slate-200 p-6">

          <div className="flex items-center gap-3 mb-5">

            <div className="bg-blue-100 p-2 rounded-lg">

              <UserRound className="text-blue-700" />

            </div>

            <h2 className="text-xl font-semibold text-slate-800">

              Patient Selection

            </h2>

          </div>

          <label className="block text-sm font-medium text-slate-700 mb-2">

            Patient ID

          </label>

          <input

            className="
              w-full
              rounded-xl
              border
              border-slate-300
              bg-white
              p-3
              shadow-sm
              focus:outline-none
              focus:ring-4
              focus:ring-blue-100
              focus:border-blue-600
              transition
            "

            placeholder="Enter Patient ID"

            value={patientId}

            onChange={(e) => setPatientId(e.target.value)}

          />

        </section>

        {/* ===========================
            Encounter Form
        ============================ */}

        {patientId && (

          <section className="bg-white rounded-2xl shadow-md border border-slate-200 p-6">

            <h2 className="text-xl font-semibold text-slate-800 mb-5">

              New Clinical Encounter

            </h2>

            <EncounterForm

              patientId={patientId}

              onResult={setResult}

            />

          </section>

        )}

        {/* ===========================
            AI Results
        ============================ */}

        {result && (

          <section className="bg-white rounded-2xl shadow-md border border-slate-200 p-6">

            <h2 className="text-xl font-semibold text-slate-800 mb-6">

              Clinical AI Assessment

            </h2>

            <ClinicalResult

              result={result}

            />

          </section>

        )}

      </main>

      {/* ===========================
          Footer
      ============================ */}

      <footer className="border-t border-slate-200 bg-white mt-8">

        <div className="max-w-6xl mx-auto px-4 py-6">

          <div className="flex justify-center items-center gap-2 text-sm text-slate-600">

            <ShieldCheck
              size={18}
              className="text-green-600"
            />

            <span>

              MedicalAI provides clinical decision support. Final clinical decisions remain the responsibility of qualified healthcare professionals.

            </span>

          </div>

        </div>

      </footer>

    </div>

  );

}

export default App;