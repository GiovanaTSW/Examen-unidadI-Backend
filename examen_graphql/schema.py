import strawberry


@strawberry.type
class Instructor:
    nombre: str


@strawberry.type
class Taller:
    nombre: str
    instructor: Instructor
    cupo: int
    activo: bool


@strawberry.input
class AgregarTallerInput:
    nombre: str
    instructor: str
    cupo: int
    activo: bool


lista_talleres: list[Taller] = [
    Taller(
        nombre="Python para backend",
        instructor=Instructor(nombre="Ana López"),
        cupo=20,
        activo=True,
    ),
    Taller(
        nombre="Introducción a Docker",
        instructor=Instructor(nombre="Carlos Ruiz"),
        cupo=15,
        activo=False,
    ),
    Taller(
        nombre="Consultas con GraphQL",
        instructor=Instructor(nombre="Ana López"),
        cupo=25,
        activo=True,
    ),
]


@strawberry.type
class Query:
    @strawberry.field
    def talleres(self) -> list[Taller]:
        return lista_talleres

    @strawberry.field
    def taller(self, nombre: str) -> Taller | None:
        for item in lista_talleres:
            if item.nombre == nombre:
                return item
        return None

    @strawberry.field
    def talleres_activos(self) -> list[Taller]:
        return [item for item in lista_talleres if item.activo]


@strawberry.type
class Mutation:
    @strawberry.mutation
    def agregar_taller(self, taller: AgregarTallerInput) -> Taller:
        nuevo = Taller(
            nombre=taller.nombre,
            instructor=Instructor(nombre=taller.instructor),
            cupo=taller.cupo,
            activo=taller.activo,
        )
        lista_talleres.append(nuevo)
        return nuevo


schema = strawberry.Schema(query=Query, mutation=Mutation)
