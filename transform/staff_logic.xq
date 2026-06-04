xquery version "3.1";

let $staff := doc("../extract/staff/all_staff_raw.xml")//person

return <riks_staff> {

    for $s in $staff

    let $iid := $s/intressent_id/text()

    return
        <staff>
            <iid>{ $iid }</iid>
            <name>
                <first_name>{ $s/tilltalsnamn/text() }</first_name>
                <last_name>{ $s/efternamn/text() }</last_name>
            </name>
            <party>{ $s/parti/text() }</party>
            <status>{ $s/status/text() }</status>

            <img_url>{ $s/bild_url_80/text() }</img_url>
            
            <assignments>
            {
                for $u in $s/personuppdrag/uppdrag
                order by $u/from descending
                return
                    <assignment>
                        <role>{ $u/roll_kod/text() }</role>
                        <task>{ $u/uppgift/text() }</task>
                        <from>{ fn:substring($u/from, 1, 10) }</from>
                        <to>{ fn:substring($u/tom, 1, 10) }</to>
                    </assignment>
            }
            </assignments>
        </staff>
}
</riks_staff>