xquery version "3.1";

declare namespace custom = "http://riksdagsinfo.se/votes";

let $votes := doc("../extract/votes/votes_enriched.xml")//votering

return <riks_votes 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:noNamespaceSchemaLocation="votes_logic.xq_out.xsd"
    xmlns:custom="http://riksdagsinfo.se/votes"> {

    for $v in $votes
    where exists($v/intressent_id)
    return
        <vote>
            <iid>{ $v/intressent_id/text() }</iid>
            <doc_id>{ $v/dok_id/text() }</doc_id>
            <result>{ $v/rost/text() }</result>
            <point>{ $v/punkt/text() }</point>
            <custom:title>{ $v/custom:title/text() }</custom:title>
            <custom:url>{ $v/custom:url/text() }</custom:url>
        </vote>
}
</riks_votes>