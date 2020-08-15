package com.conference.assistant.springboot.conferenceassistantspringboot.domain.user;

import com.conference.assistant.springboot.conferenceassistantspringboot.domain.BaseTimeEntity;
import com.conference.assistant.springboot.conferenceassistantspringboot.domain.team.Team;
import lombok.*;

import javax.persistence.*;

@Getter
@NoArgsConstructor
@Entity
@Setter
public class User extends BaseTimeEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name="user_id")
    private Long id;

    @Column(nullable = false)
    private String email;

    @Column(nullable = false)
    private String name;

    @Column(nullable = false)
    private String picture;

    @Enumerated(EnumType.STRING)
    @Column(nullable = false)
    private Status status;

    // User.team이 연관관계의 주인 (등록, 수정 o- 다수인 쪽이 주인)
    @ManyToOne
    @JoinColumn(name="team_id")
    private Team team;

    @Builder
    public User(String email, String name, String picture, Status status, Team team) {
        this.email = email;
        this.name = name;
        this.picture = picture;
        this.status = status;
        this.team = team;
    }

    public User update(String name, String picture){
        this.name = name;
        this.picture = picture;
        return this;
    }
}
