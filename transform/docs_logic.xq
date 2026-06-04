xquery version "3.1";

let $docs := doc("../extract/docs/curr_docs_raw.xml")//dokument

return <riks_docs> {

    for $d in $docs
    where exists($d/dokintressent)
    order by $d/datum descending
    return  
        <doc>
            <iid>{ $d/dokintressent/intressent/intressent_id/text() }</iid>
            <id>{ $d/dok_id/text() }</id>
            <title>{ $d/titel/text() }</title>
            <date>{ $d/datum/text() }</date>
            <dok_url>{ $d/dokument_url_html/text() }</dok_url>
        </doc>
}
</riks_docs>