def controle(n, c):
    if c == n - 1:
        print(f'Parabens Julie! Voce tomou todos os {n} comprimidos!')
        return 0

    print(f'Voce ja tomou {c + 1} comprimidos, restam {n - (c + 1)}.')

    controle(n, c  +  1)

controle(18, 0)


