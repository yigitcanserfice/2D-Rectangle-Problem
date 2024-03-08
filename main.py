import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from UI import  problem
from TestProblems import problems
from MakePackage import MakePackage
from Node import Rect

def sort(rects:list[tuple], sort_attr:str='width') -> list[tuple]:
    """ Dikdörtgenleri sırala """

    sort_types = {"width": 0, "height": 1, "max": 2, "area": 3}
    if sort_attr == 'none':
        return rects

    attr = [r + (max(r), r[0]*r[1]) for r in rects]
    sort_attr_index = sort_types.get(sort_attr, 0)
    attr.sort(key=lambda x: x[sort_attr_index], reverse=True)
    return [x[:2] for x in attr]
def draw(rects:list[Rect], figsize:tuple=(7,7)) -> None:
    """ Dikdörtgenlerin hepsini çiz """
    _, ax = plt.subplots(figsize=figsize)

    ax.set_xlim([0,rects[0].fit.w])
    ax.set_ylim([0,rects[0].fit.h])
    plt.locator_params(axis="both", integer=True, tight=True)

    for r in rects:
        if not r.fit:
            continue
        draw_rectangle(ax, r)

    plt.show()
def draw_rectangle(ax, rect: Rect) -> None:
    """ Dikdörtgen çiz """
    box = Rectangle(rect.fit.origin, rect.w, rect.h, fc='lightblue',ec='black',alpha=1.0)
    ax.add_patch(box)

if __name__ == "__main__":

    #dims = problems[2] #Test edilen veriler.
    dims = problem
    size = (20, 20)

    dims = sort(dims, sort_attr="max")
    rects = [Rect(d) for d in dims]

    p = MakePackage(*size)

    rects = p.fit(rects)
    draw(rects)

