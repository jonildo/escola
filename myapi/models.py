from django.db import models
class Base(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True,
                                        db_column='t_____criacao',
                                        db_comment='Data de inclusao do objeto')
    data_atualizacao = models.DateTimeField(auto_now=True,
                                            db_column='t_____ulat',
                                            db_comment='Data de alteração do objeto')
    ativo = models.BooleanField(default=True,
                                db_column='f_____ativo',
                                db_comment='Indicador se objeto está ativo')

    class Meta:
        abstract = True

class CursoTrilha(Base):
    id = models.BigAutoField(primary_key=True, 
                             db_column='ccurtrsequencial',
                             db_comment='Chave da tabela tbcursotrilha')
    id_curso = models.ForeignKey('Curso', on_delete=models.RESTRICT, 
                                 db_column='ccursosequencial',
                                 db_comment='Chave de ligação com curso')
    id_trilha = models.ForeignKey('Trilha', on_delete=models.RESTRICT, 
                                  db_column='ctrilhsequencial',
                                  db_comment='Chave de ligação com trilha')

    class Meta:
        verbose_name = 'CursoTrilha'
        verbose_name_plural = 'CursoTrilhas'
        unique_together = ('id_trilha', 'id_curso')
        db_table = "tbcursotrilha"
        indexes = [
            models.Index(fields=['id'], name='pcurtrchave'),
            models.Index(fields=['id_trilha', 'id_curso'], name='ucurtrchave'),
            models.Index(fields=['id_trilha'], name='icurtridtrilha'),
            models.Index(fields=['id_curso'], name='icurtridcurso'),
        ]

    def __str__(self):
        return 'Trilha: ' + str(self.id_trilha) + ', Curso: ' + str(self.id_curso)

class Trilha(Base):
    id = models.BigAutoField(primary_key=True, 
                             db_column='ctrilhsequencial',
                             db_comment='Chave da tabela tbtrilha')
    nome = models.CharField(max_length=50, unique=True,
                            blank=False, null=False, 
                            db_column='ntrilhnome',
                            db_comment='Nome da trilha')
    valor_trilha = models.DecimalField(max_digits=9, decimal_places=2,
                                       blank=False, null=False,
                                       db_column='vtrilhpreco',
                                       db_comment='Valor da trilha')
    descricao = models.TextField(blank=False, null=False,
                                 db_column='etrildescricao',
                                 db_comment='Descrição da trilha')
    publico_alvo = models.TextField(blank=False, null=False,
                                    db_column='etrilpublico',
                                    db_comment='Público alvo da Trilha')
    carga_horaria = models.IntegerField(db_column='atrilcarga',
                                        db_comment='Carga horária da Trilha')

    class Meta:
        verbose_name = 'Trilha'
        verbose_name_plural = 'Trilhas'
        db_table = 'tbtrilha'
        indexes = [
            models.Index(fields=['id'], name='ptrilhchave'),
            models.Index(fields=['nome'], name='utrilhnome'),
        ]

    def __str__(self):
        return self.nome

class Curso(Base):
    id = models.BigAutoField(primary_key=True, 
                             db_column='ccursosequencial',
                             db_comment='Chave da tabela tbcurso')
    nome = models.CharField(max_length=50, unique=True,
                            blank=False, null=False,
                            db_column='ncursonome',
                            db_comment='Nome do curso')
    valor_curso = models.DecimalField(max_digits=9, decimal_places=2,
                                      blank=False, null=False,
                                      db_column='vcurso_preco',
                                      db_comment='Valor do curso')
    descricao = models.TextField(blank=False, null=False,
                                 db_column='ecursodescricao',
                                 db_comment='Descrição do curso')
    publico_alvo = models.TextField(blank=False, null=False,
                                    db_column='ecurpublico',
                                    db_comment='Público alvo do curso')
    carga_horaria = models.IntegerField(db_column='acursocarga',
                                        db_comment='Carga horária do curso')

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        db_table = 'tbcurso'
        indexes = [
            models.Index(fields=['id'], name='pcursochave'),
            models.Index(fields=['nome'], name='ucursonome'),
        ]

    def __str__(self):
        return self.nome

class Turma(Base):
    TURNO_CHOICES = [
        ('M', 'Manhã'),
        ('T', 'Tarde'),
        ('N', 'Noite'),
    ]

    id = models.BigAutoField(primary_key=True, db_column='cturmasequencial', db_comment='Identificador da Turma')
    id_curso = models.ForeignKey('Curso', on_delete=models.RESTRICT, db_column='ccursosequencial',
                                 related_name='curso_participa_turma', blank=False, null=False)
    professor = models.CharField(max_length=50, blank=False, null=False, db_column='nturmaprofessor',
                                 db_comment='Nome do Professor')
    turno = models.CharField(max_length=1, blank=False, null=False, db_column='cturmaturno',
                             db_comment='Turno da Turma', choices=TURNO_CHOICES)
    seg = models.BooleanField(default=False, db_column='fturmasegunda',
                              db_comment='Indicador se acontece nas segundas feiras')
    ter = models.BooleanField(default=False, db_column='fturmaterca',
                              db_comment='Indicador se acontece nas terças feiras')
    qua = models.BooleanField(default=False, db_column='fturmaquarta',
                              db_comment='Indicador se acontece nas quartas feiras')
    qui = models.BooleanField(default=False, db_column='fturmaquinta',
                              db_comment='Indicador se acontece nas quintas feiras')
    sex = models.BooleanField(default=False, db_column='fturmasexta',
                              db_comment='Indicador se acontece nas sextas feiras')
    sab = models.BooleanField(default=False, db_column='fturmasabado',
                              db_comment='Indicador se acontece nos sábados')
    inicio = models.DateField(blank=False, null=False, db_column='dturmainicio',
                              db_comment='Data do início da turma')
    final = models.DateField(blank=False, null=False, db_column='dturmafinal',
                             db_comment='Data do final da turma')
    horario = models.CharField(max_length=13, blank=False, null=False, db_column='eturmahorario',
                               db_comment='Horário da turma')

    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
        db_table = 'tbturma'
        indexes = [
            models.Index(fields=['id'], name='pturmachave'),
            models.Index(fields=['id_curso'], name='fturmacurso'),
        ]

    def __str__(self):
        return f'Curso: {self.id_curso}, Início: {self.inicio}'
