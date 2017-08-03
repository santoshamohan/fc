#! /usr/bin/env python
"""
End members used in fractional cover.
Josh Sixsmith is the person to talk to about this code...

This file has been modified to only have the '2014_07_23' version
For older versions of the endmembers, see
https://github.com/GeoscienceAustralia/ga-neo-landsat-processor/blob/develop/gaip/endmembers.py

    Contacts:

        * Peter Scarth; peter.scarth@qld.gov.au
        * Josh Sixsmith; joshua.sixsmith@ga.gov.au
"""
import numpy


def sum_weight():
    """
    Retrieves the sum to one weighting constraint used for deriving the
    fractional components of a Landsat (5TM/7ETM+) image for '2014_07_23'.

    .. note::

        Scarth 20090810 14:06:35 CEST
        Define the weight of the sum to one constraint
        This value determined how well the resulting fractions will sum to 100%
        I typically determine this by running the unmixing against field data for
        a number of values, picking the best one

    :return:
        A floating point value representing the sum to one weighting
        constraint.
    """
    return 1.0


def endmember_version():
    return '2017_06_09'


def get_endmembers(sum_to_one_weight):
    """
    Gives green, dead1, dead2 and bare fractions
    Note the last row is the sum to one constraint value

    :param sum_to_one_weight:
    :return:
    """

    return numpy.array([
        [1.362599111127997704e-02, 1.899105692485177424e-02, 2.083777822709348068e-02, 8.380957579921338024e-03],
        [-2.446327204065648631e-02, -3.809941789487282515e-02, -3.459198157309664040e-02, -3.986877402379570418e-02],
        [2.260387510909207809e-02, 2.257607331884509821e-02, 3.217754444926401031e-02, 2.672548243768423093e-02],
        [1.067578150297253670e-01, 1.106023766633856126e-01, 1.129505069171332227e-01, 1.078852574667506503e-01],
        [-4.457782269331668212e-01, -4.738205399291306463e-01, -4.603414595798733244e-01, -4.690447656530716269e-01],
        [-9.619076501188508765e-02, -6.254929089773256234e-02, -5.978215122515505298e-02, -6.805555727903871144e-02],
        [-1.435851659374183242e-01, -1.744872562382195069e-01, -1.550869441473547994e-01, -1.454242139238743625e-01],
        [-1.162987031161560186e-01, -1.013814645798433167e-01, -8.738987273462167638e-02, -8.196117383328116457e-02],
        [6.868916631237938220e-02, 1.079739091165016068e-01, 1.061793567347660006e-01, 1.185208781198726635e-01],
        [2.774828825069160579e-02, 4.035013015045491036e-02, 4.119753949920693104e-02, 3.656073844770124648e-02],
        [8.929664803272635565e-02, 9.810588859066075862e-02, 1.016273871805938034e-01, 9.959471438437160484e-02],
        [1.752191501070425039e-01, 1.713975590914473268e-01, 1.667531834617300701e-01, 1.643650249256555784e-01],
        [-4.250334946769704011e-03, -1.391235982949552870e-02, -1.674696959859526407e-02, -4.062527508752453165e-02],
        [-3.425666771770396468e-01, -3.562254330401838920e-01, -3.578740303687703017e-01, -3.676304238868066676e-01],
        [-1.381953411869872861e-01, -1.696790559729413617e-01, -1.410344446630532600e-01, -1.438449699693192807e-01],
        [-4.331980281155715234e-02, -6.264895963247062161e-02, -5.290229212711207440e-02, -5.061848062858745334e-02],
        [1.597290616004793939e-01, 1.136815650691953977e-01, 9.323955914169437809e-02, 1.004127403618805953e-01],
        [8.354712392748252225e-02, 9.370699960991038524e-02, 9.029921734556488333e-02, 1.013829975046597887e-01],
        [2.266663618589471463e-01, 2.263895289743048655e-01, 2.310089522488674996e-01, 2.319466907107494147e-01],
        [-3.900486281860062604e-02, -9.071044848073250844e-02, -9.804268973127387710e-02, -1.013590187664134834e-01],
        [-2.634591956577337149e-02, -2.502923668260697079e-02, -3.960459854300258514e-02, -4.791495035581800482e-02],
        [-4.584432286790217637e-01, -4.677989492668088722e-01, -5.122665058107737091e-01, -5.013207051730687036e-01],
        [-1.648671086268057029e-01, -1.465912321308048272e-01, -1.569240668604758582e-01, -1.458645048859924520e-01],
        [8.887678196637684852e-03, 1.766040012699007095e-02, 4.053915301998685383e-02, 5.797266554240281672e-02],
        [1.426190045192837763e-01, 1.484004070661879837e-01, 1.485444300993546130e-01, 1.512126208899423063e-01],
        [-6.699986851005208799e-02, -5.502865447987727310e-02, -4.643828090336998143e-02, -4.732199728766835201e-02],
        [-6.603506396208384116e-03, -1.406274723537563522e-03, 4.115246184124066176e-03, -1.365546212935316549e-03],
        [-6.321374945400587420e-02, -1.024820858184821992e-01, -1.013414282403568845e-01, -9.320363932090197645e-02],
        [-3.372701353768651211e-01, -3.335781584496718688e-01, -3.251844536398877383e-01, -3.135241418531750091e-01],
        [2.209759051241939193e-02, 6.321078276161855303e-02, 4.536165491778242076e-02, 3.651977867157995411e-02],
        [1.583738437990394599e-01, 2.166644279084959379e-01, 1.968089046025394140e-01, 2.059898943768734558e-01],
        [-7.196888349490357384e-02, -1.231351224261720834e-01, -1.405793347346748212e-01, -1.352530021359704404e-01],
        [1.723277953528074280e-01, 1.226132411757348550e-01, 1.513228433306091358e-01, 1.330983396809611863e-01],
        [-1.968678509319562453e-01, -1.769906431170200911e-01, -1.761169574946728211e-01, -1.851352552697170251e-01],
        [-3.377878070729570248e-01, -3.737104819654674115e-01, -3.616433172208137203e-01, -3.552976997253287084e-01],
        [4.770288780774099152e-02, 4.837805525311157651e-02, 4.397708232648959298e-02, 4.162370482562190860e-02],
        [5.959423055359574367e-02, 7.548873880344360299e-02, 8.349690238341066217e-02, 9.452592007619246839e-02],
        [-2.002041437564197612e-01, -2.213161715620922676e-01, -2.325424028187378089e-01, -2.494086588587931530e-01],
        [4.273198125797958435e-02, 4.987055764199513352e-02, 6.561933662556579394e-02, 7.962196260024263783e-02],
        [-1.223576408814649602e-01, -1.368150679996098240e-01, -1.359244106874965830e-01, -1.407194983188775894e-01],
        [2.541823435970747558e-01, 2.938763129987109202e-01, 3.089053755514483135e-01, 3.188577342726977570e-01],
        [-1.500074857570478926e-01, -1.724851884973902238e-01, -1.852416809161037403e-01, -1.911957996895069234e-01],
        [-8.415992587724736851e-02, -9.943303854889627702e-02, -1.043070582952159708e-01, -1.023241033555151863e-01],
        [9.453715334457962749e-02, 1.100367734909045297e-01, 1.027769400331143140e-01, 9.566708315221406078e-02],
        [-4.237054428333697498e-02, -5.437019170281935654e-02, -5.391050889386403422e-02, -5.550645779101331251e-02],
        [9.585630410744831742e-02, 9.067089143918320715e-02, 9.687882955867906098e-02, 8.387107838869303778e-02],
        [1.708367753691383273e-01, 2.014255514216609089e-01, 2.012629236404977762e-01, 1.945387068133117292e-01],
        [1.835081952466011690e-01, 1.983090007440392322e-01, 1.855799728667132387e-01, 1.920962510995214145e-01],
        [2.997514804026993329e-01, 3.326887784707634466e-01, 3.357407774514332144e-01, 3.399324445901791281e-01],
        [3.747036818942146019e-01, 3.913471503687873665e-01, 3.891039097504336297e-01, 3.930518844063159989e-01],
        [3.628819299140489257e-02, 4.956596051836025668e-02, 6.250522762049463832e-02, 7.038397872663457178e-02],
        [3.600596477428306269e-02, 3.910857039567228188e-02, 1.737672481285707990e-02, 6.090796861141795776e-03],
        [-3.195865669811464027e-01, -3.433048714335798501e-01, -3.401868830303064195e-01, -3.375348855951140759e-01],
        [-3.557384598734649739e-01, -3.609920940352501217e-01, -3.543311776043654993e-01, -3.694164416659695971e-01],
        [-2.839725024018697197e-01, -3.289132370687339324e-01, -3.311416466191929309e-01, -3.209958849142701132e-01],
        [1.695910961412837592e-01, 1.597530508727890985e-01, 9.709420045954081369e-02, 9.673954403448065120e-02],
        [-1.395790054356613186e-01, -9.792932428385141275e-02, -9.949950163884385690e-02, -8.389941684616963880e-02],
        [2.267563151004223232e-01, 2.579726771307483402e-01, 2.377699217997832903e-01, 2.115791708647778713e-01],
        [3.101700656757097607e-01, 3.145533700695304358e-01, 2.954106728027016127e-01, 2.777238101047382335e-01],
        [sum_to_one_weight, sum_to_one_weight, sum_to_one_weight, sum_to_one_weight]
    ])
