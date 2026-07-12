interface Props{

    result:any;

}


function ClinicalResult({
    result
}:Props){


return (

<div>


<h2>
Clinical AI Assessment
</h2>


<h3>
Triage
</h3>

<pre>
{result.triage_result}
</pre>



<h3>
Knowledge Support
</h3>

<pre>
{result.knowledge_result}
</pre>



<h3>
Clinical Note
</h3>

<pre>
{result.clinical_note}
</pre>



</div>


)


}


export default ClinicalResult;