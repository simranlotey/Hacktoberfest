<?php
if(isset($_POST['submitZoneAfrica']))
{
  $date = new DateTime("now", new DateTimeZone($_POST['forAfrica']) );
    $_Current_Time=$date->format('Y-m-d H:i:s');
    $_Current_Time_Zone=$_POST['forAfrica'];
}
if(isset($_POST['submitZoneAmerica']))
{

  $date = new DateTime("now", new DateTimeZone($_POST['forAmerica']) );
    $_Current_Time=$date->format('Y-m-d H:i:s');
    $_Current_Time_Zone=$_POST['forAmerica'];
}
if(isset($_POST['submitZoneArctic']))
{

  $date = new DateTime("now", new DateTimeZone($_POST['forArctic']) );
    $_Current_Time=$date->format('Y-m-d H:i:s');
    $_Current_Time_Zone=$_POST['forArctic'];
}
if(isset($_POST['submitZoneAsia']))
{

  $date = new DateTime("now", new DateTimeZone($_POST['forAsia']) );
    $_Current_Time=$date->format('Y-m-d H:i:s');
    $_Current_Time_Zone=$_POST['forAsia'];
}
if(isset($_POST['submitZoneAtlantic']))
{

  $date = new DateTime("now", new DateTimeZone($_POST['forAtlantic']) );
    $_Current_Time=$date->format('Y-m-d H:i:s');
    $_Current_Time_Zone=$_POST['forAtlantic'];
}
if(isset($_POST['submitZoneEurope']))
{

  $date = new DateTime("now", new DateTimeZone($_POST['forEurope']) );
    $_Current_Time=$date->format('Y-m-d H:i:s');
    $_Current_Time_Zone=$_POST['forEurope'];
}
if(isset($_POST['submitZoneIndian']))
{

  $date = new DateTime("now", new DateTimeZone($_POST['forIndian']) );
    $_Current_Time=$date->format('Y-m-d H:i:s');
    $_Current_Time_Zone=$_POST['forIndian'];
}
if(isset($_POST['submitZonePacific']))
{

  $date = new DateTime("now", new DateTimeZone($_POST['forPacific']) );
    $_Current_Time=$date->format('Y-m-d H:i:s');
    $_Current_Time_Zone=$_POST['forPacific'];
}
if(isset($_POST['submitZoneOthers']))
{

  $date = new DateTime("now", new DateTimeZone($_POST['forOthers']) );
    $_Current_Time=$date->format('Y-m-d H:i:s');
    $_Current_Time_Zone=$_POST['forOthers'];
}
 ?>
<!DOCTYPE html>
<html>
<head><title>World Time and Date Consolidatede</title>
<style>
select {
  display: inline-block;
}</style>
</head>
<body>
<div style="display:flex;height:100%;width:100%;">
  <div style="height:100%;width:100%;padding-left:40px;">
<div id="divForAfrica" style="background-color:#b33d1c;color:white;height:11%;width:50%;border-style: ridge;padding:30px;">
<form method="post" id="africa">
  <label for="Time Zones">Time Zones For Africa</label>
<select name="forAfrica">Asia/Kolkata
<option value='Asia/Kolkata' selected>Select one of these regions</option>
<option value='Africa/Algiers'>Africa/Algiers</option>
<option value='Africa/Gaborone'>Africa/Gaborone</option>
<option value='Africa/Douala'>Africa/Douala</option>
<option value='Africa/Bangui'>Africa/Bangui</option>
<option value='Africa/Ndjamena'>Africa/Ndjamena</option>
<option value='Africa/Kinshasa'>Africa/Kinshasa</option>
<option value='Africa/Djibouti'>Africa/Djibouti</option>
<option value='Africa/Cairo'>Africa/Cairo</option>
<option value='Africa/Malabo'>Africa/Malabo</option>
<option value='Africa/Asmara'>Africa/Asmara</option>
<option value='Africa/Addis_Ababa'>Africa/Addis_Ababa</option>
<option value='Africa/Libreville'>Africa/Libreville</option>
<option value='Africa/Banjul'>Africa/Banjul</option>
<option value='Africa/Accra'>Africa/Accra</option>
<option value='Africa/Conakry'>Africa/Conakry</option>
<option value='Africa/Bissau'>Africa/Bissau</option>
<option value='Africa/Abidjan'>Africa/Abidjan</option>
<option value='Africa/Nairobi'>Africa/Nairobi</option>
<option value='Africa/Maseru'>Africa/Maseru</option>
<option value='Africa/Monrovia'>Africa/Monrovia</option>
<option value='Africa/Tripoli'>Africa/Tripoli</option>,
<option value='Africa/Blantyre'>Africa/Blantyre</option>
<option value='Africa/Bamako'>Africa/Bamako</option>
<option value='Africa/Nouakchott'>Africa/Nouakchott</option>
<option value='Africa/Casablanca'>Africa/Casablanca</option>
<option value='Africa/Maputo'>Africa/Maputo</option>
<option value='Africa/Windhoek'>Africa/Windhoek</option>
<option value='Africa/Niamey'>Africa/Niamey</option>
<option value='Africa/Lagos'>Africa/Lagos</option>
<option value='Africa/Brazzaville'>Africa/Brazzaville</option>
<option value='Africa/Kigali'>Africa/Kigali</option>
<option value='Africa/Sao_Tome'>Africa/Sao_Tome</option>
<option value='Africa/Dakar'>Africa/Dakar</option>
<option value='Africa/Freetown'>Africa/Freetown</option>
<option value='Africa/Mogadishu'>Africa/Mogadishu</option>
<option value='Africa/Johannesburg'>Africa/Johannesburg</option>
<option value='Africa/Juba'>Africa/Juba</option>
<option value='Africa/Khartoum'>Africa/Khartoum</option>
<option value='Africa/Mbabane'>Africa/Mbabane</option>
<option value='Africa/Dar_es_Salaam'>Africa/Dar_es_Salaam</option>
<option value='Africa/Lome'>Africa/Lome</option>
<option value='Africa/Tunis'>Africa/Tunis</option>
<option value='Africa/Kampala'>Africa/Kampala</option>
<option value='Africa/El_Aaiun'>Africa/El_Aaiun</option>
<option value='Africa/Lusaka'>Africa/Lusaka</option>
<option value='Africa/Harare'>Africa/Harare</option>
</select>
<input type="submit" name="submitZoneAfrica" value="Submit"/>
</form>
</div>

<div id="divForAmerica" style="background-color:#de408a;color:white;height:11%;width:50%;border-style: ridge;padding:30px;">
<form method="post" id="america">
  <label for="Time Zones">Time Zones For America</label>
<select name="forAmerica">
<option value='Asia/Kolkata' selected>Select one of these regions</option>
<option value='America/Nassau'>America/Nassau</option>
<option value='America/Belize'>America/Belize</option>
<option value='America/Noronha'>America/Noronha</option>
<option value='America/Tortola'>America/Tortola</option>
<option value='America/St_Johns'>America/St_Johns</option>
<option value='America/Cayman'>America/Cayman</option>
<option value='America/Santiago'>America/Santiago</option>
<option value='America/Bogota'>America/Bogota</option>
<option value='America/Costa_Rica'>America/Costa_Rica</option>
<option value='America/Havana'>America/Havana</option>
<option value='America/Curacao'>America/Curacao</option>
<option value='America/Dominica'>America/Dominica</option>
<option value='America/Santo_Domingo'>America/Santo_Domingo</option>
<option value='America/Guayaquil'>America/Guayaquil</option>
<option value='America/El_Salvador'>America/El_Salvador</option>
<option value='America/Cayenne'>America/Cayenne</option>
<option value='America/Godthab'>America/Godthab</option>
<option value='America/Grenada'>America/Grenada</option>
<option value='America/Guadeloupe'>America/Guadeloupe</option>
<option value='America/Guatemala'>America/Guatemala</option>
<option value='America/Guyana'>America/Guyana</option>
<option value='America/Port-au-Prince'>America/Port-au-Prince</option>
<option value='America/Tegucigalpa'>America/Tegucigalpa</option>
<option value='America/Jamaica'>America/Jamaica</option>
<option value='America/Martinique'>America/Martinique</option>
<option value='America/Mexico_City'>America/Mexico_City</option>
<option value='America/Montserrat'>America/Montserrat</option>
<option value='America/Managua'>America/Managua</option>
<option value='America/Panama'>America/Panama</option>
<option value='America/Asuncion'>America/Asuncion</option>
<option value='America/Lima'>America/Lima</option>
<option value='America/Puerto_Rico'>America/Puerto_Rico</option>
<option value='America/St_Kitts'>America/St_Kitts</option>
<option value='America/St_Lucia'>America/St_Lucia</option>
<option value='America/Marigot'>America/Marigot</option>
<option value='America/Miquelon'>America/Miquelon</option>
<option value='America/St_Vincent'>America/St_Vincent</option>
<option value='America/Lower_Princes'>America/Lower_Princes</option>
<option value='America/Paramaribo'>America/Paramaribo</option>
<option value='America/Port_of_Spain'>America/Port_of_Spain</option>
<option value='America/Grand_Turk'>America/Grand_Turk</option>
<option value='America/St_Thomas'>America/St_Thomas</option>
<option value='America/New_York'>America/New_York</option>
<option value='America/Montevideo'>America/Montevideo</option>
<option value='America/Caracas'>America/Caracas</option>
</select>
<input type="submit" name="submitZoneAmerica" value="Submit"/>
</form>
</div>
<!--

 -->

 <div id="divForArctic" style="background-color:#dede40;color:white;height:11%;width:50%;border-style: ridge;padding:30px;">
 <form method="post" id="arctic">
   <label for="Time Zones">Time Zones For Arctic</label>
 <select name="forArctic">
 <option value='Asia/Kolkata' selected>Select one of these regions</option>
<option value='Arctic/Longyearbyen'>Arctic/Longyearbyen</option>
 </select>
 <input type="submit" name="submitZoneArctic" value="Submit"/>
 </form>
 </div>

 <!--

 -->
 <div id="divForAsia" style="background-color:#de4062;color:white;height:11%;width:50%;border-style: ridge;padding:30px;">
 <form method="post" id="asia">
   <label for="Time Zones">Time Zones For Asia</label>
 <select name="forAsia">
 <option value='Asia/Kolkata' selected>Select one of these regions</option>
<option value='Asia/Thimphu'>Asia/Thimphu</option>
<option value='Asia/Phnom_Penh'>Asia/Phnom_Penh</option>
<option value='Asia/Shanghai'>Asia/Shanghai</option>,
<option value='Asia/Nicosia'>Asia/Nicosia</option>
<option value='Asia/Dili'>Asia/Dili</option>
<option value='Asia/Tbilisi'>Asia/Tbilisi</option>
<option value='Asia/Hong_Kong'>Asia/Hong_Kong</option>
<option value='Asia/Kolkata'>Asia/Kolkata</option>
<option value='Asia/Jakarta'>Asia/Jakarta</option>
<option value='Asia/Tehran'>Asia/Tehran</option>
<option value='Asia/Baghdad'>Asia/Baghdad</option>
<option value='Asia/Jerusalem'>Asia/Jerusalem</option>
<option value='Asia/Tokyo'>Asia/Tokyo</option>
<option value='Asia/Amman'>Asia/Amman</option>
<option value='Asia/Almaty'>Asia/Almaty</option>
<option value='Asia/Kuwait'>Asia/Kuwait</option>
<option value='Asia/Bishkek'>Asia/Bishkek</option>
<option value='Asia/Vientiane'>Asia/Vientiane</option>
<option value='Asia/Beirut'>Asia/Beirut</option>
<option value='Asia/Macau'>Asia/Macau</option>
<option value='Asia/Kuala_Lumpur'>Asia/Kuala_Lumpur</option>
<option value='Asia/Ulaanbaatar'>Asia/Ulaanbaatar</option>
<option value='Asia/Rangoon'>Asia/Rangoon</option>
<option value='Asia/Kathmandu'>Asia/Kathmandu</option>
<option value='Asia/Pyongyang'>Asia/Pyongyang</option>
<option value='Asia/Muscat'>Asia/Muscat</option>
<option value='Asia/Karachi'>Asia/Karachi</option>
<option value='Asia/Gaza'>Asia/Gaza</option>
<option value='Asia/Manila'>Asia/Manila</option>
<option value='Asia/Qatar'>Asia/Qatar</option>
<option value='Asia/Riyadh'>Asia/Riyadh</option>
<option value='Asia/Singapore'>Asia/Singapore</option>
<option value='Asia/Seoul'>Asia/Seoul</option>
<option value='Asia/Colombo'>Asia/Colombo</option>
<option value='Asia/Damascus'>Asia/Damascus</option>
<option value='Asia/Taipei'>Asia/Taipei</option>
<option value='Asia/Dushanbe'>Asia/Dushanbe</option>
<option value='Asia/Bangkok'>Asia/Bangkok</option>
<option value='Asia/Ashgabat'>Asia/Ashgabat</option>
<option value='Asia/Samarkand'>Asia/Samarkand</option>
<option value='Asia/Ho_Chi_Minh'>Asia/Ho_Chi_Minh</option>
<option value='Asia/Aden'>Asia/Aden</option>
 </select>
 <input type="submit" name="submitZoneAsia" value="Submit"/>
 </form>
 </div>
<!--

 -->
 <div id="divForAtlantic" style="background-color:#de40a9;color:white;height:11%;width:50%;border-style: ridge;padding:30px;">
 <form method="post" id="atlantic">
   <label for="Time Zones">Time Zones For Atlantic</label>
 <select name="forAtlantic">
 <option value='Asia/Kolkata' selected>Select one of these regions</option>
 <option value='Atlantic/Cape_Verde'>Atlantic/Cape_Verde</option>
  <option value='Atlantic/Stanley'>Atlantic/Stanley</option>
  <option value='Atlantic/Faroe'>Atlantic/Faroe</option>
  <option value='Atlantic/Reykjavik'>Atlantic/Reykjavik</option>
  <option value='Atlantic/St_Helena'>Atlantic/St_Helena</option>
  <option value='Atlantic/South_Georgia'>Atlantic/South_Georgia</option>
  </select>
  <input type="submit" name="submitZoneAtlantic" value="Submit"/>
  </form>
  </div>
<!--

 -->

</div>
<div style="height:100%;width:100%;padding-right:180px;">

<?php
if(isset($_Current_Time))
{
  echo "<div id='selectedTImezone' style='text-align: center;background-color:black;color:white;border-style: ridge;height:50%;width:100%;padding:30px;'>";
  echo "<h2>Time Zone : ".$_Current_Time_Zone."</h2>";
  echo "<h2>Current Date and Time : ".$_Current_Time."</h2>";
  echo "</div>";

}

 ?>

     <div id="divForEurope" style="background-color:#a540de;color:white;height:11%;width:100%;border-style: ridge;padding:30px;">
     <form method="post" id="europe">
       <label for="Time Zones">Time Zones For Europe</label>
     <select name="forEurope">
     <option value='Asia/Kolkata' selected>Select one of these regions</option>
     <option value='Europe/Minsk'>Europe/Minsk</option>
     <option value='Europe/Zagreb'>Europe/Zagreb</option>
     <option value='Europe/Prague'>Europe/Prague</option>
     <option value='Europe/Copenhagen'>Europe/Copenhagen</option>
     <option value='Europe/Tallinn'>Europe/Tallinn</option>
     <option value='Europe/Helsinki'>Europe/Helsinki</option>
     <option value='Europe/Paris'>Europe/Paris</option>
     <option value='Europe/Berlin'>Europe/Berlin</option>
     <option value='Europe/Gibraltar'>Europe/Gibraltar</option>
     <option value='Europe/Athens'>Europe/Athens</option>
     <option value='Europe/Guernsey'>Europe/Guernsey</option>
     <option value='Europe/Budapest'>Europe/Budapest</option>
     <option value='Europe/Dublin'>Europe/Dublin</option>
     <option value='Europe/Isle_of_Man'>Europe/Isle_of_Man</option>
     <option value='Europe/Rome'>Europe/Rome</option>
     <option value='Europe/Jersey'>Europe/Jersey</option>
     <option value='Europe/Riga'>Europe/Riga</option>
     <option value='Europe/Vaduz'>Europe/Vaduz</option>
     <option value='Europe/Vilnius'>Europe/Vilnius</option>
     <option value='Europe/Luxembourg'>Europe/Luxembourg</option>
     <option value='Europe/Skopje'>Europe/Skopje</option>
     <option value='Europe/Malta'>Europe/Malta</option>
     <option value='Europe/Chisinau'>Europe/Chisinau</option>
     <option value='Europe/Monaco'>Europe/Monaco</option>
     <option value='Europe/Podgorica'>Europe/Podgorica</option>
     <option value='Europe/Amsterdam'>Europe/Amsterdam</option>
     <option value='Europe/Oslo'>Europe/Oslo</option>
     <option value='Europe/Warsaw'>Europe/Warsaw</option>
     <option value='Europe/Lisbon'>Europe/Lisbon</option>
     <option value='Europe/Bucharest'>Europe/Bucharest</option>
     <option value='Europe/Kaliningrad'>Europe/Kaliningrad</option>
     <option value='Europe/San_Marino'>Europe/San_Marino</option>
     <option value='Europe/Belgrade'>Europe/Belgrade</option>
     <option value='Europe/Bratislava'>Europe/Bratislava</option>
     <option value='Europe/Ljubljana'>Europe/Ljubljana</option>
     <option value='Europe/Madrid'>Europe/Madrid</option>
     <option value='Europe/Stockholm'>Europe/Stockholm</option>
     <option value='Europe/Zurich'>Europe/Zurich</option>
     <option value='Europe/Istanbul'>Europe/Istanbul</option>
     <option value='Europe/Kiev'>Europe/Kiev</option>
     <option value='Europe/London'>Europe/London</option>
    </select>
    <input type="submit" name="submitZoneEurope" value="Submit"/>
    </form>
    </div>


    <!--

     -->

      <div id="divForIndian" style="background-color:#40deb3;color:white;height:11%;width:100%;border-style: ridge;padding:30px;">
      <form method="post" id="indian">
        <label for="Time Zones">Time Zones For Indian</label>
      <select name="forIndian">
      <option value='Asia/Kolkata' selected>Select one of these regions</option>
      <option value='Indian/Chagos'>Indian/Chagos</option>
      <option value='Indian/Christmas'>Indian/Christmas</option>
      <option value='Indian/Cocos'>Indian/Cocos</option>
      <option value='Indian/Comoro'>Indian/Comoro</option>
      <option value='Indian/Kerguelen'>Indian/Kerguelen</option>
      <option value='Indian/Antananarivo'>Indian/Antananarivo</option>
      <option value='Indian/Maldives'>Indian/Maldives</option>
      <option value='Indian/Mauritius'>Indian/Mauritius</option>
      <option value='Indian/Mayotte'>Indian/Mayotte</option>
      <option value='Indian/Reunion'>Indian/Reunion</option>
      <option value='Indian/Mahe'>Indian/Mahe</option>
   </select>
   <input type="submit" name="submitZoneIndian" value="Submit"/>
   </form>
   </div>

    <!--

     -->

      <div id="divForPacific" style="background-color:#7740de;color:white;height:11%;width:100%;border-style: ridge;padding:30px;">
      <form method="post" id="pacific">
        <label for="Time Zones">Time Zones For Pacific</label>
      <select name="forPacific">
      <option value='Asia/Kolkata' selected>Select one of these regions</option>
      <option value='Pacific/Rarotonga'>Pacific/Rarotonga</option>
      <option value='Pacific/Fiji'>Pacific/Fiji</option>
      <option value='Pacific/Tahiti'>Pacific/Tahiti</option>
      <option value='Pacific/Guam'>Pacific/Guam</option>
      <option value='Pacific/Tarawa'>Pacific/Tarawa</option>
      <option value='Pacific/Majuro'>Pacific/Majuro</option>
      <option value='Pacific/Chuuk'>Pacific/Chuuk</option>
      <option value='Pacific/Nauru'>Pacific/Nauru</option>
      <option value='Pacific/Noumea'>Pacific/Noumea</option>
      <option value='Pacific/Auckland'>Pacific/Auckland</option>
      <option value='Pacific/Niue'>Pacific/Niue</option>
      <option value='Pacific/Norfolk'>Pacific/Norfolk</option>
      <option value='Pacific/Saipan'>Pacific/Saipan</option>
      <option value='Pacific/Palau'>Pacific/Palau</option>
      <option value='Pacific/Port_Moresby'>Pacific/Port_Moresby</option>
      <option value='Pacific/Pitcairn'>Pacific/Pitcairn</option>
      <option value='Pacific/Apia'>Pacific/Apia</option>
      <option value='Pacific/Guadalcanal'>Pacific/Guadalcanal</option>
      <option value='Pacific/Fakaofo'>Pacific/Fakaofo</option>
      <option value='Pacific/Tongatapu'>Pacific/Tongatapu</option>
      <option value='Pacific/Funafuti'>Pacific/Funafuti</option>
      <option value='Pacific/Johnston'>Pacific/Johnston
      <option value='Pacific/Johnston'>Pacific/Johnston</option>
      <option value='Pacific/Efate'>Pacific/Efate</option>
      <option value='Pacific/Wallis'>Pacific/Wallis</option>
   </select>
   <input type="submit" name="submitZonePacific" value="Submit"/>
   </form>
   </div>
   <div id="divForOthers" style="background-color:#1cb35c;color:white;height:11%;width:100%;border-style: ridge;padding:30px;">
   <form method="post" id="others">
     <label for="Time Zones">Time Zones For Others</label>
   <select name="forOthers">
   <option value='Asia/Kolkata' selected>Select one of these regions</option>
   	<option value='UTC'>UTC</option>
   </select>
   <input type="submit" name="submitZoneOthers" value="Submit"/>
   </form>
   </div>
</div>
</div>
</body>
</html>
