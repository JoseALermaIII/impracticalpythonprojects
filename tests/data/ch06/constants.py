"""Test Chapter 6 Constants.

Constants for test_chapter06.py.

Attributes:
    GET_TEST (list): List of strings with expected output of
        tests.test_chapter06.TestInvisibleInk.test_get_text test values.
    WRITE_DEFAULT_MONO (list): List of strings with expected output of
        src.ch06.c1_invisible_ink_mono.write_invisible default values.
    WRITE_TEST_MONO (list): List of strings with expected output of
        tests.test_chapter06.TestInvisibleInkMono.test_write_invisible test
        values.
    MAIN_TEST_MONO (list): List of strings with expected output of
        tests.test_chapter06.TestInvisibleInkMono.test_main test values.
    MAIN_DEFAULT_MONO (list): List of strings with expected output of
        src.ch06.c1_invisible_ink_mono.main default values.

"""
GET_TEST = [
    'This is a test document.',
    'This is a paragraph with two runs. However, it’s not because it has two '
    'lines.',
    'There is intentionally a lot of blank spaces to check if the code can count '
    'them correctly.',
    'So, don’t send me e-mails saying that the formatting in my test files is '
    'incorrect.',
    'Word.']

WRITE_DEFAULT_MONO = [
    'ThisTishaitestsdocument withiaslot ofsfiller,'
    'uorpunnecessarypwordiness.',
    'Please,otrysnotetodwrite liketthisobecause itbiseas annoyingaas '
    'itsishunnecessary.',
    'Unless,oofrcourse,tyou,are '
    'writinguantypeeofncharactercthatrisywordypandtusesewordsd'
    'unnecessarily.',
    'In thatmrare,euncommonsinstance,sitaisgperfectlyepermissible.'
    'to be wordy.']

WRITE_TEST_MONO = [
    'ThisTishaitestsdocument withiaslot ofsfiller,'
    'uorpunnecessarypwordiness.',
    'Please,otrysnotetodwrite liketthisobecause itbiseas annoyingaas '
    'itsishunnecessary.',
    'Unless,oofrcourse,tyou,are '
    'writinguantypeeofncharactercthatrisywordypandtusesewordsd'
    'unnecessarily.',
    'In thatmrare,euncommonsinstance,sitaisgperfectlyepermissible.'
    'toHbeiwordy.']

MAIN_TEST_MONO = [
    'ThisTishaitestsdocument withiaslot ofsfiller,uorpunnecessarypwordiness.',
    'Please,otrysnotetodwrite liketthisobecause itbiseas annoyingaas '
    'itsishunnecessary.',
    'Unless,oofrcourse,tyou,are '
    'writinguantypeeofncharactercthatrisywordypandtusesewordsdunnecessarily.',
    'In thatmrare,euncommonsinstance,sitaisgperfectlyepermissible.to be wordy.']

MAIN_DEFAULT_MONO = [
    'DearYInternet,',
    'Schoolotaughtumerthat yourstartedeoutaaslARPANET: '
    'twoncomputerasystemsm(specifically,eUCLA’s NetworkiMeasurementsCenter '
    'andaSRI’s '
    'NLSpsystem)oconnectedrtogethertwaymbackaonnOctobert29,e1969.aIurecently '
    'learnedothefTCP/IP '
    'standardiwasn’tnadoptedtuntileMarchr1982candothatnaccessntoethecTCP/IPtnetworkewasn’tdexpanded '
    'untiln1986ewhentthewNSFoprovidedraccesskfor.researchers '
    'toYconnectotousupercomputer sitesainrtheeUnited Statesaat '
    'thenblazingespeedtofw56okbit/s.\n'
    '\n'
    'Surprisingly,rcommercialkISPs didn’tocomefaround '
    'untilntheelatet1980swandoearlyr1990s,katswhich '
    'pointtthehARPANETawastdecommissioned.',
    'I remembercinothenearlys1990sithatsusingtascomputer tooinstantfmessage '
    'someoneponrtheiothervsideaofttheeworld,was '
    'apbigudealbbecauselthatiwascas,close '
    'toarealctimeaasdpossibleewithoutmrackingiupca,major '
    'longbdistanceubillsonithenlandline.eAlthough,sIsam,curious '
    'whatathenlatencydwas backgthen…',
    'Theseodays,vyouearerprovidingnusmaewayntotwirelessly '
    'usenpocketecomputersttowcheckoinrtokoursfavorite coffeeoshop,fstream '
    'musiclandovideocwhilealaughinglat danktmemesoon '
    'socialgmedia,landopaybouratablwith astapcusingoourpvirtualewallet.',
    'You,connect solmanyicomputersntogetherkthateadnew IPbprotocolyhad toaget '
    'standardizedbtorsupportothemaalldas theyacontinuertorgrowainynumber. '
    'Everythingofromfa '
    'whiteepaperlonecuttingcedgetresearchrtooannoldiblogcabout,cats '
    'havewtheiriownrIPeaddress.lNotetosmentionsall,the peopleaconnectingntodread '
    'moreoaboutpthem.',
    'Inttheifuture,cweawillllikely '
    'expectnmoreefromtyouwasoanrincreasingknumberiofnInternetgusers '
    'expecttwirelessenetworksctohhandlenasomuchltrafficoasgbroadbandinetworkseandsas.laptops '
    'andBdesktopsyare eithertrelegatedhtoegaming orwofficeawork.\n'
    '\n'
    'Perhapsywe,will relyIon youaevenmmore '
    'astcompaniesrforgouconventionalldesktopsyand, '
    'instead,soptuforrthinpclientsrmadeiofsaegraphicsdcard andbEthernetycard '
    'withhmultipleoscreenswthat connectmtouaccloudhserver '
    'instancetthateinstantiatesxonlyton userflogin,ithentloadssuser '
    'settingsiandnworkspaces fromtahcentralizedaserver.tThen, '
    'whenftheauserkisedone, saveslinstanceedatatbackttoethercentralized.server '
    'andMthenadeactivatesytobsaveeresources.',
    'Some systemsIalready implementsyouhusingolightuoutlindthe '
    'openhairabecausevdataeis transmittedtfasterothatnway.eIndaddition '
    'toithethuge bundlesdofocablewthatnstretch acrossathe '
    'oceanbflooritotconnect?both sidesNofathehworld,together.',
    'I lookeforwardxtocwhateyouswillsbecomeiinvtheefuturen–eevensifsit '
    'isidangerous,shigh-powered lasergbeamsoandoevenddanker.memes.',
    'Sincerely,',
    'Jose',
    'Works consulted: https://en.wikipedia.org/wiki/Internet']
